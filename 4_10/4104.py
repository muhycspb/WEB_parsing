import json
import requests
from bs4 import BeautifulSoup

session = requests.Session()

result = []


def get_soup(url: str):
    response = session.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser')


for page in range(1, 5):
    soup = get_soup(f'https://parsinger.ru/html/index4_page_{page}.html')
    names = [i.text.strip() for i in soup.select('.name_item')]
    descriptions = [[desc.strip().split(': ')[-1].strip() for desc in description.text.strip().split('\n')] for
                    description in soup.select('.description')]
    prices = [i.text.strip() for i in soup.select('.price')]

    for i in range(len(names)):
        result.append(
            {
                "Наименование": names[i],
                "Бренд": descriptions[i][0],
                "Форм-фактор": descriptions[i][1],
                "Ёмкость": descriptions[i][2],
                "Объем буферной памяти": descriptions[i][3],
                "Цена": prices[i]
            }
        )

with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
