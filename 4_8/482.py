import requests
from bs4 import BeautifulSoup


def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')


soup = get_soup('https://parsinger.ru/table/1/index.html')

rows = soup.find('table').find_all('tr')[1::]
date = []
for row in rows:
    for i in row.find_all('td'):
        if i.text not in date:
            date.append(i.text)

print(sum([float(i) for i in date]))


print()