import ast
import json
import os
import time
from pathlib import Path
from unittest.mock import Mock

import pytest


@pytest.fixture
def email_finder(tmp_path, monkeypatch):
    # The launcher runs its interactive menu at module scope, so the test compiles
    # only the option 10 branch of this repository's xosint and runs it with mocks.
    source = Path(__file__).resolve().parents[1] / "xosint"
    tree = ast.parse(source.read_text())
    option_test = ast.parse('option == "10"', mode="eval").body
    node = next((
        branch for branch in ast.walk(tree)
        if isinstance(branch, ast.If)
        and ast.dump(
            branch.test.values[0] if isinstance(branch.test, ast.BoolOp) else branch.test
        ) == ast.dump(option_test)
    ), None)
    if node is None:
        pytest.fail('xosint has no `option == "10"` branch')
    code = compile(ast.Module(body=[node], type_ignores=[]), str(source), "exec")
    monkeypatch.chdir(tmp_path)
    requests = Mock()
    prompt = Mock(side_effect=["example.com", "Élodie", "Martin"])
    namespace = dict(option="10", os=os, json=json, time=time, sleep=Mock(),
                     requests=requests, coloured_input=prompt)
    return requests, prompt, lambda: exec(code, namespace)  # skipcq: PYL-W0122


@pytest.mark.parametrize("async_run", [False, True])
def test_monid_email_finder(email_finder, monkeypatch, capsys, async_run):
    monkeypatch.setenv("MONID_API_KEY", "fake-key")
    requests, prompt, run = email_finder
    output = {"data": {"email": "elodie@example.com", "score": 95}}
    completed = {"status": "COMPLETED", "output": output}
    requests.post.return_value.status_code = 202 if async_run else 200
    requests.post.return_value.json.return_value = {"runId": "run-1"} if async_run else completed
    requests.get.return_value.json.side_effect = [{"status": "RUNNING"}, completed]

    run()

    args, kwargs = requests.post.call_args
    assert args == ("https://api.monid.ai/v1/run",)
    assert kwargs["headers"] == {
        "Authorization": "Bearer fake-key",
        "Content-Type": "application/json; charset=utf-8",
    }
    assert json.loads(kwargs["data"]) == {
        "provider": "hunterio",
        "endpoint": "/email-finder",
        "input": {"queryParams": {
            "domain": "example.com", "first_name": "Élodie", "last_name": "Martin",
        }},
    }
    assert "Élodie".encode("utf-8") in kwargs["data"]
    assert prompt.call_count == 3
    assert requests.get.call_count == (2 if async_run else 0)
    for call in requests.get.call_args_list:
        assert call.args == ("https://api.monid.ai/v1/runs/run-1",)
    assert json.loads(capsys.readouterr().out) == output


def test_monid_prints_hunter_error(email_finder, monkeypatch, capsys):
    monkeypatch.setenv("MONID_API_KEY", "fake-key")
    requests, _, run = email_finder
    error = {"errors": [{"id": "not_found", "details": "No match"}]}
    requests.post.return_value.status_code = 200
    requests.post.return_value.json.return_value = {
        "status": "COMPLETED",
        "providerResponse": {"httpStatus": 404, "error": error},
    }

    run()

    assert capsys.readouterr().out == json.dumps(error, indent=2, sort_keys=True) + "\n"


def test_email_finder_without_monid(email_finder, monkeypatch, capsys):
    monkeypatch.delenv("MONID_API_KEY", raising=False)
    requests, prompt, run = email_finder
    prompt.side_effect = ["hunter-key", "example.com", "Élodie", "Martin"]
    output = {"data": {"email": None}}
    requests.get.return_value.text = json.dumps(output)

    run()

    requests.post.assert_not_called()
    requests.get.assert_called_once_with(
        "https://api.hunter.io/v2/email-finder?domain=example.com"
        "&first_name=Élodie&last_name=Martin&api_key=hunter-key"
    )
    assert capsys.readouterr().out == (
        "[+] File written: ./hunter_io_api.txt\n"
        + json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
