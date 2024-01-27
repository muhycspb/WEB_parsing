import requests
from bs4 import BeautifulSoup


def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')


soup = get_soup('https://parsinger.ru/4.8/7/index.html')

total = 0

tds = soup.find('div').find_all('td')
print(len(tds))
for td in tds:
    td = int(td.text)
    if td % 3 == 0:
        total += td

print(total)