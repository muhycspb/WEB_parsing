from bs4 import BeautifulSoup
import requests
import lxml

total = []

for page in range(1, 5):
    response = requests.get(f'https://parsinger.ru/html/index3_page_{page}.html')

    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')

    total.append([item.text for item in soup.find_all('a', class_='name_item')])

print(total)
