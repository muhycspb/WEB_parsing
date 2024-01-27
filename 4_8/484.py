import requests
from bs4 import BeautifulSoup

def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')


soup = get_soup('https://parsinger.ru/table/5/index.html')
data = []
trs = soup.find('table').find_all('tr')[1::]
for tr in trs:
    # data.append(float(tr.find('td', class_='orange').text) *
    data.append(float(tr.find('td', class_='orange').text) * float(tr.find_all('td')[-1].text))
print(sum(data))