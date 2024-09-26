"""
loads pdf file in sys.argv[1], extracts URLs, tries to load each URL
some credits to stackoverflow.com/questions/27744210
"""

import os
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import PyPDF2


def extract_urls(filename):
    """extracts all urls from filename"""
    with open(filename, "rb") as pdf_file:
        pdf_handler = PyPDF2.PdfReader(pdf_file)
        pages = len(pdf_handler.pages)

        key = "/Annots"
        uri = "/URI"
        ank = "/A"

        for page in range(pages):
            page_object = pdf_handler.pages[page].get_object()
            if key in page_object:
                ann = page_object[key]
                for value in ann:
                    object_handler = value.get_object()
                    if uri in object_handler[ank]:
                        yield object_handler[ank][uri]


def check_http_url(link):
    """check url validity"""
    try:
        if "coreus" in link:
            return
        # print(link)
        req = Request(
            link,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
                "Accept-Encoding": "none",
                "Accept-Language": "en-US,en;q=0.8",
                "Connection": "keep-alive",
                "refere": "https://google.com",
                "cookie": """your cookie value ( you can get that from your web page) """,
            },
        )
        with urlopen(req, timeout=10) as weburl:
            if weburl.getcode() != 200:
                print("Broken " + link)
    except HTTPError as exception:
        print(str(exception) + " for " + link)


if __name__ == "__main__":
    for url in extract_urls(sys.argv[1]):
        check_http_url(url)
    print("Done")
