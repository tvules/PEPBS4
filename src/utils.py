from urllib.parse import urljoin

from bs4 import Tag
from requests import Response, Session

from exceptions import ParserFindTagException, TagAttributeException


def get_response(session: Session, *args, **kwargs) -> Response:
    response = session.get(*args, **kwargs)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response


def find_tag(soup: Tag, name=None, attrs=None, **kwargs):
    tags = find_tags(soup, name=name, attrs=attrs, limit=1, **kwargs)
    return tags[0]


def find_tags(soup: Tag, name=None, attrs=None, **kwargs):
    tags = soup.find_all(name, attrs=attrs or {}, **kwargs)
    if not tags:
        raise ParserFindTagException(f"Не найден тег {name} {attrs}.")
    return tags


def get_tag_attr(tag: Tag, name: str) -> str:
    try:
        return tag[name]
    except KeyError as ex:
        raise TagAttributeException(
            f"В теге `{tag.name}` не найден аттрибут `{ex}`."
        )


def make_url_from_href(base: str, a_tag: Tag):
    return urljoin(base, get_tag_attr(a_tag, "href"))
