import requests
from fake_useragent import UserAgent

url = 'https://parsinger.ru/img_download/img/ready/'

ua = UserAgent()

fake_ua = {'user-agent': ua.random}

for i in range(1, 161):
    with open(f'{i}.png', 'wb') as f:
        f.write(requests.get(url + f'{i}.png', headers=fake_ua, stream=True).content)
