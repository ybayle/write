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
        pdf_handler = PyPDF2.PdfFileReader(pdf_file)
        pages = pdf_handler.getNumPages()

        key = "/Annots"
        uri = "/URI"
        ank = "/A"

        for page in range(pages):
            page_object = pdf_handler.getPage(page).getObject()
            if key in page_object:
                ann = page_object[key]
                for value in ann:
                    object_handler = value.getObject()
                    if uri in object_handler[ank]:
                        yield object_handler[ank][uri]


def check_http_url(link):
    """check url validity"""
    try:
        req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=10) as weburl:
            if weburl.getcode() != 200:
                print("Broken " + link)
    except HTTPError as exception:
        print(str(exception) + " for " + link)


if __name__ == "__main__":
    for url in extract_urls(sys.argv[1]):
        check_http_url(url)
    print("Done")
