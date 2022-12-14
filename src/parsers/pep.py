import logging
from typing import List, Tuple

from bs4 import BeautifulSoup, ResultSet, Tag
from requests import RequestException, Session
from tqdm import tqdm

from constants import EXPECTED_STATUS, MAIN_PEPS_URL
from exceptions import ParserFindTagException, ParsingException, TagException
from utils import find_tag, find_tags, get_response, make_url_from_href

URL = MAIN_PEPS_URL


def get_table_from_section(soup: BeautifulSoup, section_id: str) -> Tag:
    return find_tag(find_tag(soup, "section", id=section_id), "table")


def get_table_rows(table: Tag) -> ResultSet:
    return find_tags(find_tag(table, "tbody"), "tr")


def parse_row(row: Tag) -> Tuple:
    return get_raw_status(row), get_url(row)


def get_raw_status(row: Tag) -> str:
    return find_tag(row, "abbr").text[1:]


def get_url(row: Tag) -> str:
    return make_url_from_href(URL, find_tag(row, "a"))


def get_status_from_page(soup: BeautifulSoup):
    tag = find_tag(soup, string="Status").parent
    sibling = tag.find_next_sibling()
    if sibling is None:
        raise ParserFindTagException("Не найден тег статуса.")
    return sibling.text


def pep(session: Session) -> List[Tuple[str, int]]:
    try:
        response = get_response(session, url=MAIN_PEPS_URL)
        table = get_table_from_section(
            BeautifulSoup(response.text, features="lxml"),
            section_id="numerical-index",
        )
        rows = get_table_rows(table)
    except (TagException, RequestException) as ex:
        raise ParsingException(ex) from ex

    counting, total = {}, 0
    for row in tqdm(rows):
        try:
            raw_status, url = parse_row(row)
            table_status = EXPECTED_STATUS.get(raw_status)

            if table_status is None:
                logging.warning(
                    f"Из таблицы получен неожиданный статус: "
                    f"`{raw_status}`, `{url}`."
                )

            response = get_response(session, url=url)
            actual_status = get_status_from_page(
                BeautifulSoup(response.text, features="lxml")
            )

            if table_status is not None and actual_status not in table_status:
                logging.warning(
                    f"Несовпадающий статус ({url}): "
                    f"Ожидаемые: {table_status}, "
                    f"В карточке: `{actual_status}`."
                )

            counting[actual_status] = counting.get(actual_status, 0) + 1
            total += 1

        except (TagException, RequestException) as ex:
            logging.exception(ex, stack_info=True)
            continue

    return [("Статус", "Количество"), *counting.items(), ("Total", total)]
