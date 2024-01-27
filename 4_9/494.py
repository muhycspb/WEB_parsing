import csv
import requests
from bs4 import BeautifulSoup


def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')


with open('file.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])

    for page in range(1, 5):
        soup = get_soup(f'https://parsinger.ru/html/index4_page_{page}.html')

        names = [name.text.strip() for name in soup.select('.name_item')]
        descriptions = [[desc.strip().split(': ')[-1].strip() for desc in description.text.strip().split('\n')] for
                        description in soup.select('.description')]
        prices = [price.text for price in soup.select('.price')]

        for name, description, price in zip(names, descriptions, prices):
            row = name, *description, price
            writer.writerow(row)
