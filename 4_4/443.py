from bs4 import BeautifulSoup
import lxml

with open('../index.html', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)
