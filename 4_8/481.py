import requests
from bs4 import BeautifulSoup


def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')
    else:
        return False


soup = get_soup('https://parsinger.ru/4.8/1/index.html')

for person in soup.find('table').find_all('tr')[1::]:
    column = person.find_all('td')
    name = column[0].text
    age = column[1].text
    print(f'Имя: {name}, Возраст: {age}')
