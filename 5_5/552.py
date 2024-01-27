from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while True:
        result = browser.find_element(By.ID, 'result').text
        if result != 'refresh page':
            print(result)
            break
        browser.refresh()
