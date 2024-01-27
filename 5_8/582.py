import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/1/index.html')

    for el in driver.find_elements(By.CLASS_NAME, 'buttons'):
        el.click()
        time.sleep(0.3)
        driver.switch_to.alert.accept()
        result = driver.find_element(By.ID, 'result').text
        if result:
            print(result)
            break
