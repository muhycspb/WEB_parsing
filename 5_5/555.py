from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    total = 0
    for i in browser.find_elements(By.CLASS_NAME, 'parent'):
        if i.find_element(By.CLASS_NAME, 'checkbox').is_enabled():
            total += int(i.find_element(By.TAG_NAME, 'textarea').text)
    print(total)