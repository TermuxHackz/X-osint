#!/usr/bin/env python3
import os
import re
import time
import asyncio
import pexpect
import subprocess
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# OpenTelemetry setup
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.asyncio import AsyncioInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Initialize tracing
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
trace_provider = TracerProvider()
trace_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
trace.set_tracer_provider(trace_provider)

# Instrument asyncio and requests
AsyncioInstrumentor().instrument()
RequestsInstrumentor().instrument()

# Get tracer
tracer = trace.get_tracer(__name__)

TOKEN = os.environ.get("XOSINT_BOT_TOKEN")
if not TOKEN:
    raise SystemExit("XOSINT_BOT_TOKEN is not set")

WORKDIR = "/root/X-osint"
PYTHON = "/root/X-osint/venv/bin/python"
XOSINT = "/root/X-osint/xosint"
KEYS_FILE = "/root/X-osint/numandcage_keys.txt"
SHODAN_FILE = "/root/X-osint/api.txt"
IDLE_TIMEOUT = 15 * 60

ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")
CTRL_RE = re.compile(r"\x1b\][0-9;]*.*?\x07")
DISCLAIMER_RE = re.compile(r"accept the disclaimer", re.IGNORECASE)
MODNOTFOUND_RE = re.compile(r"ModuleNotFoundError: No module named ['\"]([^'\"]+)['\"]")
IMPORTERR_RE = re.compile(r"ImportError: No module named ['\"]([^'\"]+)['\"]")

MODULE_TO_PIP = {
    "bs4": "beautifulsoup4",
    "PIL": "pillow",
    "cv2": "opencv-python",
    "googleapiclient": "google-api-python-client",
    "dns": "dnspython",
    "Crypto": "pycryptodome",
    "telegram": "python-telegram-bot",
}

MODULE_TO_APT = {
    "tkinter": ["python3-tk"],
    "Tkinter": ["python3-tk"],
}

auto_installed = {}

sessions = {}
pending_actions = {}

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton("IP"), KeyboardButton("Email"), KeyboardButton("Дорк")],
        [KeyboardButton("Субдомены"), KeyboardButton("Утечка email"), KeyboardButton("Утечка домен")],
        [KeyboardButton("Утечка юзер"), KeyboardButton("Дарквеб"), KeyboardButton("Телефон1")],
        [KeyboardButton("Телефон2"), KeyboardButton("Справка"), KeyboardButton("Сброс")],
        [KeyboardButton("Стоп"), KeyboardButton("Меню"), KeyboardButton("Отмена")],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Выберите действие",
)

LABEL_TO_ACTION = {
    "IP": "IP",
    "Email": "Email",
    "Dork": "Dork",
    "Subdomain": "Subdomain",
    "Breach Email": "Breach Email",
    "Breach Domain": "Breach Domain",
    "Breach User": "Breach User",
    "Darkweb": "Darkweb",
    "Phone1": "Phone1",
    "Phone2": "Phone2",
    "Help": "Help",
    "Reset": "Reset",
    "Stop": "Stop",
    "Menu": "Menu",
    "Cancel": "Cancel",
    "Дорк": "Dork",
    "Субдомены": "Subdomain",
    "Утечка email": "Breach Email",
    "Утечка домен": "Breach Domain",
    "Утечка юзер": "Breach User",
    "Дарквеб": "Darkweb",
    "Телефон1": "Phone1",
    "Телефон2": "Phone2",
    "Справка": "Help",
    "Сброс": "Reset",
    "Стоп": "Stop",
    "Меню": "Menu",
    "Отмена": "Cancel",
}

ACTION_PROMPTS = {
    "IP": "Введите IP: пример `8.8.8.8`",
    "Email": "Введите email: пример `user@example.com`",
    "Dork": "Введите dork (последнее число = count): пример `site:example.com 10`",
    "Subdomain": "Введите домен (опционально путь к списку): `example.com /root/X-osint/subdomains.txt`",
    "Breach Email": "Введите email для утечек: `user@example.com`",
    "Breach Domain": "Введите домен для утечек: `example.com`",
    "Breach User": "Введите username для утечек: `username`",
    "Darkweb": "Введите запрос для darkweb: `example query`",
    "Phone1": "Введите телефон и опциональные ключи: `+15551234567 [ipqualityscore] [opencage] [vonage_key] [vonage_secret]`",
    "Phone2": "Введите телефон и опциональные ключи: `15551234567 [numverify] [opencage]`",
}


def clean_output(text: str) -> str:
    if not text:
        return ""
    text = CTRL_RE.sub("", text)
    text = ANSI_RE.sub("", text)
    text = text.replace("\r", "")
    return text.strip()


def chunk_text(text: str, limit: int = 3500):
    return [text[i:i + limit] for i in range(0, len(text), limit)]


def spawn_session():
    proc = pexpect.spawn(
        f"{PYTHON} {XOSINT}",
        encoding="utf-8",
        timeout=5,
        maxread=200000,
        codec_errors="ignore",
        cwd=WORKDIR,
    )
    proc.delaybeforesend = 0.05
    return proc


def read_output(proc, max_wait: float = 3.0) -> str:
    end_time = time.time() + max_wait
    chunks = []
    while True:
        try:
            chunk = proc.read_nonblocking(size=4096, timeout=0.2)
            if chunk:
                chunks.append(chunk)
                end_time = time.time() + 0.7
        except pexpect.TIMEOUT:
            if time.time() > end_time:
                break
        except pexpect.EOF:
            break
    return "".join(chunks)


def run_sequence(inputs, step_wait: float = 3.5, final_wait: float = 2.0) -> str:
    proc = spawn_session()
    output = read_output(proc, 2.5)
    if DISCLAIMER_RE.search(output):
        proc.sendline("yes")
        output += read_output(proc, 2.5)
    for line in inputs:
        proc.sendline(line)
        output += read_output(proc, step_wait)
    output += read_output(proc, final_wait)
    try:
        proc.terminate(force=True)
    except Exception:
        pass
    return output


def pip_install(pkg: str) -> tuple[bool, str]:
    try:
        res = subprocess.run(
            [PYTHON, "-m", "pip", "install", pkg],
            capture_output=True,
            text=True,
            check=False,
        )
        ok = res.returncode == 0
        out = (res.stdout or "") + "\n" + (res.stderr or "")
        return ok, out.strip()
    except Exception as exc:
        return False, str(exc)


def apt_install(pkgs: list[str]) -> tuple[bool, str]:
    try:
        res = subprocess.run(
            ["apt-get", "update"],
            capture_output=True,
            text=True,
            check=False,
        )
        res2 = subprocess.run(
            ["apt-get", "install", "-y", *pkgs],
            capture_output=True,
            text=True,
            check=False,
        )
        ok = res2.returncode == 0
        out = (res.stdout or "") + "\n" + (res2.stdout or "") + "\n" + (res2.stderr or "")
        return ok, out.strip()
    except Exception as exc:
        return False, str(exc)


def detect_missing_module(text: str) -> str | None:
    m = MODNOTFOUND_RE.search(text) or IMPORTERR_RE.search(text)
    if not m:
        return None
    mod = m.group(1).strip()
    if not re.match(r"^[A-Za-z0-9_.-]+$", mod):
        return None
    return mod


def resolve_module(mod: str) -> tuple[str, str | list[str]]:
    root = mod.split(".")[0]
    if root in MODULE_TO_APT:
        return "apt", MODULE_TO_APT[root]
    return "pip", MODULE_TO_PIP.get(root, root)


def format_install_result(ok: bool, method: str, pkg, out: str) -> str:
    tail = "\n".join(out.splitlines()[-8:]) if out else ""
    status = "OK" if ok else "FAILED"
    summary = f"Auto dependency install ({method} {pkg}): {status}"
    if tail:
        return f"{summary}\n{tail}"
    return summary


def maybe_auto_install(text: str) -> tuple[bool, str | None]:
    mod = detect_missing_module(text)
    if not mod:
        return False, None
    root = mod.split(".")[0]
    prev = auto_installed.get(root)
    if prev:
        if prev.get("ok"):
            return False, f"Dependency '{root}' already installed; skipping."
        if time.time() - prev.get("ts", 0) < 600:
            return False, f"Dependency '{root}' install failed recently; retry later."
    method, pkg = resolve_module(mod)
    if method == "apt":
        ok, out = apt_install(pkg)  # type: ignore[arg-type]
        auto_installed[root] = {"ts": time.time(), "ok": ok}
        return ok, format_install_result(ok, "apt", " ".join(pkg), out)
    ok, out = pip_install(str(pkg))
    auto_installed[root] = {"ts": time.time(), "ok": ok}
    return ok, format_install_result(ok, "pip", pkg, out)


def write_keys(lines):
    with open(KEYS_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")


def write_shodan_key(key: str):
    with open(SHODAN_FILE, "w", encoding="utf-8") as f:
        f.write(f"{key}\n")


def get_session(chat_id: int):
    sess = sessions.get(chat_id)
    if sess and sess["proc"].isalive():
        return sess
    proc = spawn_session()
    sess = {"proc": proc, "last": time.time()}
    sessions[chat_id] = sess
    return sess


def stop_session(chat_id: int):
    sess = sessions.pop(chat_id, None)
    if not sess:
        return
    try:
        sess["proc"].terminate(force=True)
    except Exception:
        pass


async def send_chunks(message, text: str):
    clean = clean_output(text)
    if not clean:
        await message.reply_text("(no output; tool may be waiting for input)")
        return
    for part in chunk_text(clean):
        await message.reply_text(part)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with tracer.start_as_current_span("cmd_start") as span:
        chat_id = update.effective_chat.id
        span.set_attribute("chat_id", chat_id)
        sess = get_session(chat_id)
        sess["last"] = time.time()
        output = await asyncio.to_thread(read_output, sess["proc"], 2.5)
        if output:
            await send_chunks(update.message, output)
        await update.message.reply_text(
            "X-osint bot is ready. Type menu numbers or answers as shown by the tool.\n"
            "Use /reset to restart the session, /stop to end it.\n\n"
            "Use only with authorization; you are responsible for any queries.",
            reply_markup=MAIN_KEYBOARD,
        )


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Select an action:", reply_markup=MAIN_KEYBOARD)


async def cmd_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if pending_actions.pop(chat_id, None):
        await update.message.reply_text("Pending action canceled.")
    else:
        await update.message.reply_text("Nothing to cancel.")


async def cmd_reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with tracer.start_as_current_span("cmd_reset") as span:
        chat_id = update.effective_chat.id
        span.set_attribute("chat_id", chat_id)
        stop_session(chat_id)
        sess = get_session(chat_id)
        sess["last"] = time.time()
        output = await asyncio.to_thread(read_output, sess["proc"], 2.5)
        if output:
            await send_chunks(update.message, output)
        await update.message.reply_text("Session reset.")


async def cmd_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    stop_session(chat_id)
    await update.message.reply_text("Session stopped.")


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start, /menu, /reset, /stop, /help, /cancel\n\n"
        "Auto commands:\n"
        "/ip <ip>\n"
        "/email <email>\n"
        "/dork <query> [count]\n"
        "/subdomain <domain> [list_path]\n"
        "/breach_email <email>\n"
        "/breach_domain <domain>\n"
        "/breach_user <username>\n"
        "/darkweb <query>\n"
        "/phone1 <+number> [ipqualityscore] [opencage] [vonage_key] [vonage_secret]\n"
        "/phone2 <number> [numverify] [opencage]\n"
        "\nAuto-fix:\n"
        "If a missing Python module error appears, the bot will try to install it automatically.\n"
    )


async def handle_button_action(update: Update, label: str) -> bool:
    chat_id = update.effective_chat.id
    action = LABEL_TO_ACTION.get(label)
    if not action:
        return False
    if action == "Help":
        await cmd_help(update, None)  # type: ignore[arg-type]
        return True
    if action == "Reset":
        await cmd_reset(update, None)  # type: ignore[arg-type]
        return True
    if action == "Stop":
        await cmd_stop(update, None)  # type: ignore[arg-type]
        return True
    if action == "Menu":
        await cmd_menu(update, None)  # type: ignore[arg-type]
        return True
    if action == "Cancel":
        await cmd_cancel(update, None)  # type: ignore[arg-type]
        return True
    if action in ACTION_PROMPTS:
        pending_actions[chat_id] = action
        await update.message.reply_text(ACTION_PROMPTS[action])
        return True
    return False


async def handle_pending_action(update: Update, action: str, text: str) -> bool:
    chat_id = update.effective_chat.id
    value = text.strip()
    if not value:
        await update.message.reply_text("Введите значение.")
        return True

    if action == "IP":
        pending_actions.pop(chat_id, None)
        await run_auto(update, ["1", value], 3.5, 2.5)
        return True
    if action == "Email":
        pending_actions.pop(chat_id, None)
        await run_auto(update, ["2", value], 3.5, 2.5)
        return True
    if action == "Dork":
        pending_actions.pop(chat_id, None)
        parts = value.split()
        count = "5"
        if parts and parts[-1].isdigit():
            count = parts[-1]
            query = " ".join(parts[:-1])
        else:
            query = value
        if not query:
            await update.message.reply_text("Usage: /dork <query> [count]")
            return True
        outfile = f"/root/X-osint/dork_{int(time.time())}.txt"
        await run_auto(update, ["14", query, count, outfile], 5.0, 2.5)
        await update.message.reply_text(f"Saved dork output to {outfile}")
        return True
    if action == "Subdomain":
        pending_actions.pop(chat_id, None)
        parts = value.split()
        domain = parts[0]
        list_path = parts[1] if len(parts) > 1 else "/root/X-osint/subdomains.txt"
        await run_auto(update, ["13", domain, list_path], 4.0, 2.5)
        return True
    if action == "Breach Email":
        pending_actions.pop(chat_id, None)
        await run_auto(update, ["16", "1", value], 4.0, 2.5)
        return True
    if action == "Breach Domain":
        pending_actions.pop(chat_id, None)
        await run_auto(update, ["16", "2", value], 4.0, 2.5)
        return True
    if action == "Breach User":
        pending_actions.pop(chat_id, None)
        await run_auto(update, ["16", "3", value], 4.0, 2.5)
        return True
    if action == "Darkweb":
        pending_actions.pop(chat_id, None)
        await run_auto(update, ["17", value, "n"], 5.0, 2.5)
        return True
    if action == "Phone1":
        pending_actions.pop(chat_id, None)
        parts = value.split()
        phone = parts[0]
        if len(parts) >= 5:
            write_keys(parts[1:5])
        await run_auto(update, ["18", "24", "1", phone], 5.0, 2.5)
        return True
    if action == "Phone2":
        pending_actions.pop(chat_id, None)
        parts = value.split()
        phone = parts[0]
        if len(parts) >= 3:
            write_keys(parts[1:3])
        await run_auto(update, ["18", "24", "2", phone], 5.0, 2.5)
        return True
    return False


async def run_auto(update: Update, seq, step_wait: float = 3.5, final_wait: float = 2.0):
    with tracer.start_as_current_span("run_auto") as span:
        span.set_attribute("chat_id", update.effective_chat.id)
        span.set_attribute("sequence", str(seq))
        output = await asyncio.to_thread(run_sequence, seq, step_wait, final_wait)
        installed, msg = await asyncio.to_thread(maybe_auto_install, output)
        if msg:
            await update.message.reply_text(msg)
        if installed:
            span.set_attribute("auto_install", True)
            output = await asyncio.to_thread(run_sequence, seq, step_wait, final_wait)
        await send_chunks(update.message, output)


async def cmd_ip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with tracer.start_as_current_span("cmd_ip") as span:
        span.set_attribute("chat_id", update.effective_chat.id)
        if not context.args:
            await update.message.reply_text("Usage: /ip <ip>")
            return
        ip = context.args[0]
        span.set_attribute("ip", ip)
        await run_auto(update, ["1", ip], 3.5, 2.5)


async def cmd_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with tracer.start_as_current_span("cmd_email") as span:
        span.set_attribute("chat_id", update.effective_chat.id)
        if not context.args:
            await update.message.reply_text("Usage: /email <email>")
            return
        email = context.args[0]
        span.set_attribute("email", email)
        await run_auto(update, ["2", email], 3.5, 2.5)


async def cmd_dork(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /dork <query> [count]")
        return
    count = "5"
    if context.args[-1].isdigit():
        count = context.args[-1]
        query = " ".join(context.args[:-1])
    else:
        query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Usage: /dork <query> [count]")
        return
    outfile = f"/root/X-osint/dork_{int(time.time())}.txt"
    await run_auto(update, ["14", query, count, outfile], 5.0, 2.5)
    await update.message.reply_text(f"Saved dork output to {outfile}")


async def cmd_subdomain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /subdomain <domain> [list_path]")
        return
    domain = context.args[0]
    list_path = context.args[1] if len(context.args) > 1 else "/root/X-osint/subdomains.txt"
    await run_auto(update, ["13", domain, list_path], 4.0, 2.5)


async def cmd_breach_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /breach_email <email>")
        return
    email = context.args[0]
    await run_auto(update, ["16", "1", email], 4.0, 2.5)


async def cmd_breach_domain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /breach_domain <domain>")
        return
    domain = context.args[0]
    await run_auto(update, ["16", "2", domain], 4.0, 2.5)


async def cmd_breach_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /breach_user <username>")
        return
    username = context.args[0]
    await run_auto(update, ["16", "3", username], 4.0, 2.5)


async def cmd_darkweb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /darkweb <query>")
        return
    query = " ".join(context.args)
    await run_auto(update, ["17", query, "n"], 5.0, 2.5)


async def cmd_phone1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /phone1 <+number> [ipqualityscore] [opencage] [vonage_key] [vonage_secret]")
        return
    phone = context.args[0]
    if len(context.args) >= 5:
        write_keys(context.args[1:5])
    await run_auto(update, ["18", "24", "1", phone], 5.0, 2.5)


async def cmd_phone2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /phone2 <number> [numverify] [opencage]")
        return
    phone = context.args[0]
    if len(context.args) >= 3:
        write_keys(context.args[1:3])
    await run_auto(update, ["18", "24", "2", phone], 5.0, 2.5)


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with tracer.start_as_current_span("handle_text") as span:
        chat_id = update.effective_chat.id
        span.set_attribute("chat_id", chat_id)
        sess = get_session(chat_id)
        sess["last"] = time.time()
        text = update.message.text
        span.set_attribute("text_length", len(text))
        label = text.strip()
        pending = pending_actions.get(chat_id)
        if pending:
            if await handle_pending_action(update, pending, text):
                return
        if await handle_button_action(update, label):
            return
        await asyncio.to_thread(sess["proc"].sendline, text)
        output = await asyncio.to_thread(read_output, sess["proc"], 4.0)
        installed, msg = await asyncio.to_thread(maybe_auto_install, output)
        if msg:
            await update.message.reply_text(msg)
        if installed:
            stop_session(chat_id)
            span.set_attribute("dependency_installed", True)
            await update.message.reply_text("Dependency installed. Please repeat your last command.")
        await send_chunks(update.message, output)


async def cleanup_job(context: ContextTypes.DEFAULT_TYPE):
    now = time.time()
    for chat_id, sess in list(sessions.items()):
        if now - sess["last"] > IDLE_TIMEOUT:
            stop_session(chat_id)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("menu", cmd_menu))
    app.add_handler(CommandHandler("cancel", cmd_cancel))
    app.add_handler(CommandHandler("reset", cmd_reset))
    app.add_handler(CommandHandler("stop", cmd_stop))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("ip", cmd_ip))
    app.add_handler(CommandHandler("email", cmd_email))
    app.add_handler(CommandHandler("dork", cmd_dork))
    app.add_handler(CommandHandler("subdomain", cmd_subdomain))
    app.add_handler(CommandHandler("breach_email", cmd_breach_email))
    app.add_handler(CommandHandler("breach_domain", cmd_breach_domain))
    app.add_handler(CommandHandler("breach_user", cmd_breach_user))
    app.add_handler(CommandHandler("darkweb", cmd_darkweb))
    app.add_handler(CommandHandler("phone1", cmd_phone1))
    app.add_handler(CommandHandler("phone2", cmd_phone2))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.job_queue.run_repeating(cleanup_job, interval=300, first=300)
    app.run_polling()


if __name__ == "__main__":
    main()
