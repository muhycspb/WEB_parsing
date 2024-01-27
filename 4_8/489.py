import json
import requests
from bs4 import BeautifulSoup


def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')


soup = get_soup('https://parsinger.ru/4.8/6/index.html')

filtered_cars = []

tr = soup.find('tbody').find_all('tr')

for row in tr:
    columns = row.find_all('td')
    brand = columns[0].text
    year = int(columns[1].text)
    engine = columns[4].text
    cost = int(columns[7].text)

    if cost <= 4_000_000 and engine == "Бензиновый" and year >= 2005:
        filtered_cars.append(
            {"Марка Авто": brand, "Год выпуска": year, "Тип двигателя": engine, "Стоимость авто": cost})

sorted_cars = sorted(filtered_cars, key=lambda x: x["Стоимость авто"])

print(json.dumps(sorted_cars, indent=4, ensure_ascii=False))
