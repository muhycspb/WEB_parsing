import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/3/index.html')
    time.sleep(0.5)
    check_button = driver.find_element(By.ID, 'check')

    for span in driver.find_elements(By.CLASS_NAME, 'pin'):
        pin = span.text
        check_button.click()
        driver.switch_to.alert.send_keys(pin)
        time.sleep(0.3)
        driver.switch_to.alert.accept()
        result = driver.find_element(By.ID, 'result').text
        if result != 'Неверный пин-код':
            print(result)
            break
