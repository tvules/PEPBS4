import re
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
from requests import RequestException, Session
from tqdm import tqdm

from constants import MAIN_DOC_URL
from exceptions import ParsingException, TagException
from utils import find_tag, get_response

URL = urljoin(MAIN_DOC_URL, "download.html")


def get_download_table(soup: Tag) -> Tag:
    return find_tag(soup, "table", attrs={"class": "docutils"})


def get_download_link(soup: Tag, file_type) -> str:
    tag = find_tag(
        soup, "a", attrs={"href": re.compile(rf".+{file_type}\.zip$")}
    )
    return urljoin(URL, tag["href"])


def download_file(
    url: str,
    filename: str,
    session: Session,
    downloads_dir: Optional[Path] = None,
    chunk_size: int = 1024,
) -> None:
    response = get_response(session, url=url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    if downloads_dir is None:
        downloads_dir = Path(__file__).parent / "downloads"
    downloads_dir.mkdir(parents=True, exist_ok=True)

    with open(downloads_dir / filename, "wb") as file, tqdm(
        desc=f"Скачивание архива `{filename}`",
        total=total_size,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=chunk_size):
            bar.update(file.write(data))


def download(
    session: Session,
    downloads_dir: Path,
    file_type: str = "pdf-a4",
) -> None:
    try:
        response = get_response(session, url=URL)
        soup = BeautifulSoup(response.text, features="lxml")

        table = get_download_table(soup)
        link = get_download_link(table, file_type)
        file_name = link.split("/")[-1]

        download_file(link, file_name, session, downloads_dir)
    except (TagException, RequestException) as ex:
        raise ParsingException(ex) from ex
