import logging
from typing import List

from requests_cache import CachedSession

import parsers
from configs import configure_argument_parser, configure_logging
from constants import BASE_DIR
from exceptions import ParsingException
from outputs import control_output


def whats_new(session: CachedSession) -> List:
    return parsers.whats_new(session)


def latest_versions(session: CachedSession) -> List:
    return parsers.latest_versions(session)


def download(session: CachedSession) -> None:
    return parsers.download(
        session,
        downloads_dir=BASE_DIR / "downloads",
    )


def pep(session: CachedSession) -> List:
    return parsers.pep(session)


MODE_TO_FUNCTION = {
    "download": download,
    "latest-versions": latest_versions,
    "pep": pep,
    "whats-new": whats_new,
}


def main():
    configure_logging()

    logging.info("Парсинг запущен.")

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f"Аргументы командной строки: {args}.")

    session = CachedSession(expire_after=-1)
    if args.clear_cache:
        session.cache.clear()

    try:
        result = MODE_TO_FUNCTION[args.mode](session)
        if result is not None:
            control_output(result, args)
    except ParsingException as ex:
        logging.exception(ex, stack_info=True)

    logging.info("Парсинг завершен.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
