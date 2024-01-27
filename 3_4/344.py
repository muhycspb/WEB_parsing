import requests

url = 'https://parsinger.ru/3.4/2/index.html'

r = requests.get(url)
r.encoding = 'utf-8'
print(r.text)