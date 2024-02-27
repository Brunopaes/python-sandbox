from bs4 import BeautifulSoup
import io
import os
import requests
from tqdm import tqdm


def downloading_images(url_list, folder_path):
    image_quantity = len(os.listdir(folder_path))
    for idx, url_img in zip(
            range(image_quantity, image_quantity + len(url_list)),
            url_list
    ):
        image_bytes = requests.get(url_img).content
        with io.open(f"{folder_path}/{idx}.jpg", "wb") as file:
            file.write(image_bytes)
        file.close()


def grabbing_image_url(url_base):
    response = requests.get(url_base)
    soup = BeautifulSoup(response.content, "html5lib")

    twitter_urls = [
        img_url_.attrs.get("content") for img_url_
        in soup.find_all("meta", {"property": "og:image"})
    ]

    og_tag_urls = [
        img_url_.attrs.get("content") for img_url_
        in soup.find_all("meta", {"property": "og:image"})
    ]

    return list(set(og_tag_urls + twitter_urls))


if __name__ == '__main__':
    folder_path = r"C:\Users\Bruno\Desktop\playboy_blend"
    url_list_ = [
        "https://imgchest.com/p/o24ajwbe4lj",
        "https://imgchest.com/p/dl7p8l2jyox",
        "https://imgchest.com/p/agyvrmdz789",
        "https://imgchest.com/p/na7k83zm78d",
        "https://imgchest.com/p/92493ogv4nk",
        "https://imgchest.com/p/dl7p8x98yox",
    ]

    for base_url in tqdm(url_list_):
        img_url = grabbing_image_url(base_url)
        downloading_images(img_url, folder_path)
