from bs4 import BeautifulSoup
import requests
import lxml
import time

scheme = 'https://parsinger.ru/html/'
s = requests.Session()
total = 0


def get_soup(url: str):
    response = s.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    else:
        return False


def get_total_items(url: str):
    global total
    soup = get_soup(url)
    price = int(soup.find('span', id='price').text.split()[0])
    in_stock = int(soup.find('span', id='in_stock').text.split()[-1])
    total += price * in_stock


def surf_pages(url: str):
    '''добываем ссылки товаров со всем страниц в категории, переходим в них'''
    page = 1
    while True:
        soup = get_soup(f'{url}{page}.html')
        if soup:
            items_links = [scheme + link['href'] for link in soup.find_all('a', class_='name_item')]
            for link in items_links:
                get_total_items(link)
            page += 1
        else:
            break


def get_main_menu(url: str):
    '''добываем ссылки категорий, переходим в них'''
    soup = get_soup(url)
    nav_menu_links = [scheme + link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]
    for category in nav_menu_links:
        surf_pages(category[:-6:])
    print(total)


if __name__ == '__main__':
    start = time.time()
    get_main_menu('https://parsinger.ru/html/index1_page_1.html')
    print((time.time() - start) / 60)
