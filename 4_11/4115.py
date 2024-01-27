import requests

r = requests.get('https://parsinger.ru/4.6/1/res.json').json()

result = {}

for item in r:
    result[item['categories']] = result.get(item['categories'], 0) + int(item['article']) * int(item['description']['rating'])
print(result)