from bs4 import BeautifulSoup

import os


def read_file(file_path: str):
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()


def write_file(file_path: str, soup_file):
    with open(file_path, "w", encoding='utf-8') as f:
        no_headers = str(soup_file).replace(
            '<?xml version="1.0" encoding="utf-8"?>\n', ''
        )
        f.write(no_headers)


def soup(file_data: str):
    return BeautifulSoup(file_data, "xml").find_all("Col1")


def header_creation(tags):
    for idx, el in enumerate(tags):
        if idx + 1 < len(tags):
            if el.is_empty_element and tags[idx + 1].is_empty_element:
                el.string = "a"
                el.string.replace_with("TABELA FANTASMA")
    return tags


if __name__ == '__main__':
    # for a single file
    from bs4 import BeautifulSoup

    file = r"C:\Users\Bruno\Desktop\BMFO1 - Copy.xml"
    with open(file, "r", encoding='utf-8') as f:
        data = f.read()

    soup = BeautifulSoup(data, "xml")
    tags = soup.find_all("Col1")

    for idx, el in enumerate(tags):
        if idx + 1 < len(tags):
            if el.is_empty_element and tags[idx + 1].is_empty_element:
                el.string = "a"
                el.string.replace_with("TABELA FANTASMA")

    # save file
    with open(file, "w", encoding='utf-8') as f:
        no_headers = str(soup).replace(
            '<?xml version="1.0" encoding="utf-8"?>\n', '')
        f.write(no_headers)