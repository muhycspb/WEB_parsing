import csv
import requests
from bs4 import BeautifulSoup

session = requests.Session()


def get_soup(url: str):
    response = session.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(response.status_code)


with open('file.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
                     'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
                     'Ссылка на карточку с товаром'])

    for page in range(1, 33):
        link = f'https://parsinger.ru/html/watch/1/1_{page}.html'
        soup = get_soup(link)

        name = soup.select_one('#p_header').text
        article = soup.select_one('.article').text.split()[-1]
        description = [ul.text.split(':')[-1].strip() for ul in soup.select('#description li')]
        in_stock = soup.select_one('#in_stock').text.split(':')[-1].strip()
        price = soup.select_one('#price').text
        old_price = soup.select_one('#old_price').text

        writer.writerow((name, article, *description, in_stock, price, old_price, link))

print('Готово')
