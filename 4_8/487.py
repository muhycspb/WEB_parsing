import requests
from bs4 import BeautifulSoup


def get_soup(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')


soup = get_soup('https://parsinger.ru/table/5/index.html')
data_dict = {}
trs = soup.find('table').find_all('tr')

for i in range(15):
    data_dict[trs[0].find_all('th')[i].text] = 0


for tr in trs[1:]:
    for num, td in enumerate(tr.find_all('td')):
        data_dict[trs[0].find_all('th')[num].text] = data_dict.get(trs[0].find_all('th')[num].text, 0) + float(td.text)

data_dict = dict([(item[0], round(item[1], 3)) for item in data_dict.items()])

print(data_dict)
