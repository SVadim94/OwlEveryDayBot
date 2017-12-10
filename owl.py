"""Get today's OWL!"""
import os

from urllib.request import urlopen, Request, urlretrieve
from bs4 import BeautifulSoup


BASE_URL = "http://sovoteka.ru"


def get_owl_url():
    req = Request(BASE_URL + "/random", None, headers={"User-Agent": "Mozilla/1.0"})
    res = urlopen(req)
    html = res.read()
    bsp = BeautifulSoup(html, 'html.parser')

    # get all the results
    divs = bsp.find_all('div', class_='big')

    for div in divs:
        img = div.findChild('img')
        owl = BASE_URL + img.attrs['src']

        return owl


def main():
    """main function, gets a random owl, nuff said"""
    owl = get_owl_url()
    filename = os.path.basename(owl)
    urlretrieve(owl, filename=filename)

if __name__ == "__main__":
    main()
