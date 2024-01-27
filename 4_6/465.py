from bs4 import BeautifulSoup
import requests
import lxml


def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'lxml')
    else:
        return False


def get_art(url: str) -> int:
    soup = get_soup(url)
    return int(soup.find('p', class_='article').text.split()[-1])


def get_sum_art():
    total, page = 0, 1
    while True:
        soup = get_soup(f'https://parsinger.ru/html/index3_page_{page}.html')
        if soup:
            for item in soup.find_all('a', class_='name_item'):
                total += get_art('https://parsinger.ru/html/' + item.get('href'))
            page += 1
        else:
            break
    print(total)


if __name__ == '__main__':
    get_sum_art()
