import re
from typing import List, Tuple

from bs4 import BeautifulSoup, ResultSet, Tag
from requests import RequestException, Session

from constants import MAIN_DOC_URL
from exceptions import ParsingException, TagException
from utils import find_tag, find_tags, get_response

URL = MAIN_DOC_URL
TAG_PATTERN = r"Python (?P<version>\d\.\d+) \((?P<status>.*)\)"


def get_sidebar(soup: Tag) -> Tag:
    return find_tag(soup, "div", attrs={"class": "sphinxsidebarwrapper"})


def get_a_tags(soup: Tag) -> ResultSet:
    return find_tags(
        soup, "a", text=re.compile(TAG_PATTERN + r"|All versions")
    )


def parse_tag(tag: Tag) -> Tuple[str, str, str]:
    try:
        link = tag["href"]
    except KeyError:
        link = ""

    matched = re.search(TAG_PATTERN, tag.text)
    if matched is None:
        return link, tag.text, ""

    version, status = matched.groups()
    return link, version, status


def latest_versions(session: Session) -> List[Tuple[str, str, str]]:
    try:
        response = get_response(session, url=URL)
        soup = BeautifulSoup(response.text, features="lxml")

        sidebar = get_sidebar(soup)
        a_tags = get_a_tags(sidebar)
    except (TagException, RequestException) as ex:
        raise ParsingException(ex) from ex

    result = [("Ссылка на документацию", "Версия", "Статус")]
    for tag in a_tags:
        result.append(parse_tag(tag))

    return result
