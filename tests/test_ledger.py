"""Valida com ``bean-check`` o plano de contas de referência e o livro de exemplo."""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LEDGERS = [
    ROOT / "ledger" / "chart_of_accounts_br.beancount",
    ROOT / "examples" / "demo.beancount",
]


@pytest.mark.parametrize("path", LEDGERS, ids=lambda p: p.name)
def test_bean_check(path: Path) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "beancount.scripts.check", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
