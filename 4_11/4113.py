import requests

r = requests.get('https://parsinger.ru/downloads/get_json/res.json').json()

result = {}

for item in r:
    result[item['categories']] = result.get(item['categories'], 0) + int(item['count'])

print(result)