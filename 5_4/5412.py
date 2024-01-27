from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    result = [int(p.text) for p in browser.find_elements(By.XPATH, '//div[@class="text"]/p[2]')]
    print(sum(result))
