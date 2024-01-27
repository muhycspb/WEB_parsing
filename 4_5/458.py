from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

total = sum([float(price.text.split()[0]) for price in soup.find_all('p', class_='price')])

print(total)