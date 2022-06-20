# Парсит только от собственника, только первая страница, только Мск, только аренда
# Должен собирать объявления 1-й страницы в бд, потом, через 3 минуты проверяет заново и сверяет с уже имеющимися
# объявлениями. Если есть новые, добавляет в бд и отправляет в телегу сообщение.

import datetime
from collections import namedtuple

import bs4
import requests

InnerBlock = namedtuple('Block', 'title, price, currency, date, url')


class Block(InnerBlock):
    def __str__(self):
        return f'{self.title}\t{self.price}\t{self.currency}\t{self.date}\t{self.url}'


class AvitoParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {

        }