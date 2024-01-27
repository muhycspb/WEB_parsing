import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    for el in browser.find_elements(By.CLASS_NAME, 'form'):
        el.send_keys('some text')
    browser.find_element(By.ID, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)