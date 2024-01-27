import requests

url = 'https://parsinger.ru/3.4/1/json_weather.json'

r = requests.get(url).json()
min_t = 100
date_min_t = ''
for i in r:
    min_i = int(i['Температура воздуха'].strip('°C'))
    if min_i < min_t:
        min_t = min_i
        date_min_t = i['Дата']

print(date_min_t, min_t)