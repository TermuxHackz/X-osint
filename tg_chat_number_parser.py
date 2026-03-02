#!/usr/bin/env python3
"""Парсер телефонных номеров из Telegram-чатов.

Поддерживает:
- локальные файлы экспорта (`.json`, `.txt`, `.html`)
- ссылки на публичные чаты/каналы Telegram (`https://t.me/...`)
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
from requests import RequestException

PHONE_REGEX = re.compile(r"(?<!\w)(?:\+|00)?\d(?:[\d\s().-]{5,}\d)")
TAG_REGEX = re.compile(r"<[^>]+>")
POST_ID_REGEX = re.compile(r'data-post="[^"]+/(\d+)"')


def normalize_phone(raw: str) -> str:
    cleaned = re.sub(r"[^\d+]", "", raw.strip())

    if cleaned.startswith("00"):
        cleaned = "+" + cleaned[2:]

    if cleaned.count("+") > 1:
        cleaned = "+" + cleaned.replace("+", "")

    if "+" in cleaned and not cleaned.startswith("+"):
        cleaned = "+" + cleaned.replace("+", "")

    digits_only = cleaned.replace("+", "")
    if len(digits_only) < 7 or len(digits_only) > 15:
        return ""

    return cleaned if cleaned.startswith("+") else digits_only


def extract_text_from_json(node: object) -> Iterable[str]:
    if isinstance(node, dict):
        for value in node.values():
            yield from extract_text_from_json(value)
    elif isinstance(node, list):
        for item in node:
            yield from extract_text_from_json(item)
    elif isinstance(node, str):
        yield node


def read_text_from_file(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        return "\n".join(extract_text_from_json(data))

    return path.read_text(encoding="utf-8", errors="ignore")


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def chat_url_to_web(url: str) -> str:
    parsed = urlparse(url)
    if "t.me" not in parsed.netloc:
        raise ValueError("Поддерживаются только ссылки Telegram (t.me)")

    path_parts = [part for part in parsed.path.split("/") if part]
    if not path_parts:
        raise ValueError("Некорректная ссылка на Telegram-чат")

    # Нормализуем варианты: /name, /s/name, /name/123
    if path_parts[0] == "s" and len(path_parts) >= 2:
        chat_name = path_parts[1]
    else:
        chat_name = path_parts[0]

    return f"https://t.me/s/{chat_name}"


def strip_html(value: str) -> str:
    text = TAG_REGEX.sub(" ", value)
    return re.sub(r"\s+", " ", text)


def fetch_chat_text(chat_url: str, pages: int, timeout: int = 15) -> str:
    base_url = chat_url_to_web(chat_url)
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
    }

    all_chunks: list[str] = []
    before_id: str | None = None

    for _ in range(max(1, pages)):
        url = base_url if before_id is None else f"{base_url}?before={before_id}"
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
        except RequestException as exc:
            raise SystemExit(f"Ошибка загрузки Telegram-ссылки: {exc}") from exc

        html = response.text

        all_chunks.append(strip_html(html))

        post_ids = [int(x) for x in POST_ID_REGEX.findall(html)]
        if not post_ids:
            break
        next_before = min(post_ids)

        if before_id is not None and str(next_before) == before_id:
            break
        before_id = str(next_before)

    return "\n".join(all_chunks)


def parse_numbers(text: str) -> Counter[str]:
    results: Counter[str] = Counter()
    for match in PHONE_REGEX.findall(text):
        normalized = normalize_phone(match)
        if normalized:
            results[normalized] += 1
    return results


def save_csv(numbers: Counter[str], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["phone", "count"])
        for phone, count in numbers.most_common():
            writer.writerow([phone, count])


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Извлекает телефонные номера из файлов Telegram-чата "
            "(JSON/HTML/TXT) или по ссылке на публичный чат t.me"
        )
    )
    parser.add_argument(
        "input",
        help="Путь к файлу экспорта чата ИЛИ ссылка вида https://t.me/<chat>",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("phones.csv"),
        help="Куда сохранить результат CSV (по умолчанию phones.csv)",
    )
    parser.add_argument(
        "--json",
        dest="json_output",
        type=Path,
        help="Дополнительно сохранить результат в JSON",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Сколько страниц чата читать по ссылке (по умолчанию 1)",
    )

    args = parser.parse_args()

    if is_url(args.input):
        text = fetch_chat_text(args.input, pages=args.pages)
    else:
        input_path = Path(args.input)
        if not input_path.exists():
            raise SystemExit(f"Файл не найден: {input_path}")
        text = read_text_from_file(input_path)

    numbers = parse_numbers(text)
    save_csv(numbers, args.output)

    if args.json_output:
        args.json_output.write_text(
            json.dumps(numbers.most_common(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    print(f"Найдено уникальных номеров: {len(numbers)}")
    print(f"CSV сохранён: {args.output}")
    if args.json_output:
        print(f"JSON сохранён: {args.json_output}")


if __name__ == "__main__":
    main()
