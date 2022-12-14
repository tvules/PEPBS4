import logging
import re
from typing import List, Tuple
from urllib.parse import urljoin

from bs4 import BeautifulSoup, ResultSet, Tag
from requests import RequestException, Session
from tqdm import tqdm

from constants import MAIN_DOC_URL
from exceptions import ParserFindTagException, ParsingException, TagException
from utils import find_tag, find_tags, get_response, make_url_from_href

URL = urljoin(MAIN_DOC_URL, "whatsnew/")
TAG_PATTERN = r"What’s New In Python \d+\.\d+"


def get_a_tags(soup: Tag) -> ResultSet:
    return find_tags(soup, "a", string=re.compile(TAG_PATTERN))


def get_info_from_page(soup: Tag) -> Tuple[str, str]:
    header = find_tag(soup, "h1").text.replace("¶", "")
    try:
        tag = find_tag(
            soup,
            "dt",
            string=re.compile(r"^(editor\w*|author\w*)$", re.IGNORECASE),
        )
        editor = tag.find_next_sibling().text.strip()
    except ParserFindTagException:
        editor = ""
    return header, editor


def whats_new(session: Session) -> List[Tuple[str, str, str]]:
    try:
        response = get_response(session, url=URL)
        a_tags = get_a_tags(BeautifulSoup(response.text, features="lxml"))
    except (TagException, RequestException) as ex:
        raise ParsingException(ex) from ex

    result = [("Ссылка на статью", "Заголовок", "Редактор, Автор")]
    for tag in tqdm(a_tags):
        try:
            url = make_url_from_href(URL, tag)

            response = get_response(session, url=url)
            soup = BeautifulSoup(response.text, features="lxml")

            result.append((url, *get_info_from_page(soup)))
        except (TagException, RequestException) as ex:
            logging.exception(ex, stack_info=True)

    return result
