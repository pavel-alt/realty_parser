# Парсит только от собственника, только первая страница, только Мск, только аренда
# Должен собирать объявления 1-й страницы в бд, потом, через 3 минуты проверяет заново и сверяет с уже имеющимися
# объявлениями. Если есть новые, добавляет в бд и отправляет в телегу сообщение.

import requests     # Библиотека, делающая запросы по ссылке
from selectolax.parser import HTMLParser        # Парсер


def get_html(url):
    response = requests.get(url=url)   # Переменная = Получть данные по урлу
    html = response.text            # Узнать у Кати (м.б. преобразование данных в текст)

    tree = HTMLParser(html)     # создаем дерево для парсера, куда передаем текст запроса
    items = tree.css('div[data-maker="item"]')
    for item in items:
        print(item.css_first('h3').text())


def main():
    url = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok/1-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUjlk?f=ASgBAQICA0SSA8gQ8AeQUsDBDbr9NwJAzAgUjlme~A4UAg&user=1'


if __name__ == '__main__':
    main()
