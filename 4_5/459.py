from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://parsinger.ru/html/hdd/4/4_1.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

old_price = int(soup.find(id='old_price').text.split()[0])

price = int(soup.find(id='price').text.split()[0])

discount = round((old_price - price) * 100 / old_price, 1)

print(discount)
