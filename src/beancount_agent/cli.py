"""Interface de linha de comando do beancount-agent."""

import argparse

from beancount_agent import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="beancount-agent",
        description="Contabilidade diária movida a agentes, sobre Beancount e Fava.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    build_parser().parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
