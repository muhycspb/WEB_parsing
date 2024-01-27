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


for item in range(1, 33):
    link = f'https://parsinger.ru/html/mobile/2/2_{item}.html'
    soup = get_soup(link)

    result.append(
        {
            "categories": "mobile",
            "name": soup.select_one('#p_header').text.strip(),
            "article": soup.select_one('.article').text.split(': ')[1].strip(),
            "description": {li['id']: li.text.split(': ')[-1].strip() for li in soup.select('#description li')},
            "count": soup.select_one('#in_stock').text.split(': ')[1].strip(),
            "price": soup.select_one('#price').text.strip(),
            "old_price": soup.select_one('#old_price').text.strip(),
            "link": link
        }
    )

with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

print(f'Выполнено за {time.time() - start_time} секунд')
