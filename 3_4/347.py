import requests

r = requests.get('https://parsinger.ru/3.4/3/dialog.json').json()

users = {}


def recur(obj: dict | list) -> None:
    if type(obj) is dict:
        users[obj['username']] = users.get(obj['username'], 0) + 1
        recur(obj['comments'])
    else:
        for elem in obj:
            recur(elem)


recur(r)
print(dict(sorted(users.items(), key=lambda x: (-x[1], x[0]))))
