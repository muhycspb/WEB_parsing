import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': UserAgent().random}
session = requests.Session()


def get_soup(url: str):
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(response.status_code)


with open('file.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    for category in range(1, 6):
        for page in range(1, 5):
            soup = get_soup(f'https://parsinger.ru/html/index{category}_page_{page}.html')

            names = [name.text.strip() for name in soup.select('.name_item')]
            descriptions = [[desc.strip().split(': ')[-1].strip() for desc in description.text.strip().split('\n')] for
                            description in soup.select('.description')]
            prices = [price.text for price in soup.select('.price')]

            for name, description, price in zip(names, descriptions, prices):
                writer.writerow(name, *description, price)

print('Готово')
