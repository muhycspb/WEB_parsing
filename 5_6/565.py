from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    total = 0
    for cookie in webdriver.get_cookies():
        if cookie['name'][-1] in ('02468'):
            total += int(cookie['value'])
    print(total)
