import time
import json
import requests
from bs4 import BeautifulSoup

start_time = time.time()

session = requests.Session()

result = []


def get_soup(url: str):
    response = session.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser')


for category in range(1, 6):
    for page in range(1, 5):

        soup = get_soup(f'https://parsinger.ru/html/index{category}_page_{page}.html')
        names = [i.text.strip() for i in soup.select('.name_item')]
        descriptions = [[desc.split(': ') for desc in description.text.strip().split('\n')] for
                        description in soup.select('.description')]
        prices = [i.text.strip() for i in soup.select('.price')]

        for i in range(len(names)):
            result.append(
                {
                    "Наименование": names[i],
                    descriptions[i][0][0].strip(): descriptions[i][0][1].strip(),
                    descriptions[i][1][0].strip(): descriptions[i][1][1].strip(),
                    descriptions[i][2][0].strip(): descriptions[i][2][1].strip(),
                    descriptions[i][3][0].strip(): descriptions[i][3][1].strip(),
                    "Цена": prices[i]
                }
            )

with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

print(f'Готово, ушло {time.time() - start_time} секунд')
