from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

result = []

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    cls_txt = browser.find_elements(By.CLASS_NAME, 'text')
    for txt in cls_txt:
        result.append(sum([int(p.text) for p in txt.find_elements(By.TAG_NAME, 'p')]))
    print(sum(result))