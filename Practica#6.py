# -- coding: utf-8 --

import requests
from bs4 import BeautifulSoup

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def google_images():
    print("Ingrese un LINK para el realizar el request")
    soup = get_soup(input(""))
    t =dict()
    images = soup.find_all('img')
    t = [{'src':f"{image.get('src')}"} for image in images]
    print(f"{[src['src'] for src in t]}")

if __name__ == "__main__":
    google_images()
