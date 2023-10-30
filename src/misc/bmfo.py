from bs4 import BeautifulSoup

file = r"C:\Users\Bruno\Desktop\bmfo.xml"
with open(file, "r", encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, "xml")
tags = soup.find_all("Coll")

for idx, el in enumerate(tags):
    if idx + 1 < len(tags):
        if el.is_empty_element and tags[idx + 1].is_empty_element:
            el.string = "a"
            el.string.replace_with("TABELA FANTASMA")

# save file
with open(file, "w", encoding='utf-8') as f:
    no_headers = str(soup).replace(
        '<?xml version="1.0" encoding="utf-8"?>\n', ''
    )
    f.write(no_headers)
