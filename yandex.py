import requests
from selectolax.parser import HTMLParser


def main():
    url = 'https://realty.yandex.ru/sankt-peterburg/kupit/kvartira/dvuhkomnatnaya/vtorichniy-rynok/?win=375&clid=2296056'
    response = requests.get(url)
    html = response.text

    tree = HTMLParser(html)
    print(HTMLParser(html).html)
    script = tree.css('script')

    print(script)


if __name__ == '__main__':
    main()
