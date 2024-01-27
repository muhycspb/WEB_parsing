import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/2/index.html')
    time.sleep(0.5)

    for el in driver.find_elements(By.CLASS_NAME, 'buttons'):
        el.click()
        time.sleep(0.3)
        pin_code = driver.switch_to.alert.text

        driver.switch_to.alert.accept()

        driver.find_element(By.ID, 'input').send_keys(pin_code)
        driver.find_element(By.ID, 'check').click()

        result = driver.find_element(By.ID, 'result').text

        if result != 'Неверный пин-код':
            print(result)
            break
