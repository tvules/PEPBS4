import logging
from argparse import ArgumentParser
from logging.handlers import RotatingFileHandler
from typing import Iterable

from constants import BASE_DIR, LOG_DT_FORMAT, LOG_FORMAT, OUTPUT_CHOICES


def configure_argument_parser(
    available_modes: Iterable[str],
) -> ArgumentParser:
    parser = ArgumentParser(description="Парсер документации Python")
    parser.add_argument(
        "mode",
        choices=available_modes,
        help="Режимы работы парсера",
    )
    parser.add_argument(
        "-c",
        "--clear-cache",
        action="store_true",
        help="Очистка кеша",
    )
    parser.add_argument(
        "-o",
        "--output",
        choices=OUTPUT_CHOICES,
        help="Дополнительные способы вывода данных",
    )
    return parser


def configure_logging() -> None:
    log_dir = BASE_DIR / "logs"
    log_dir.mkdir(exist_ok=True)

    rotating_handler = RotatingFileHandler(
        log_dir / "parser.log",
        maxBytes=10**6,
        backupCount=5,
        encoding="utf-8",
    )
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DT_FORMAT,
        handlers=(rotating_handler, logging.StreamHandler()),
    )
