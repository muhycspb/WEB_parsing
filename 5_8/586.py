import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Запуск в headless режиме
chrome_options.add_argument("--disable-gpu")  # Если Windows, на других системах не нужно
chrome_options.add_argument("--window-size=1920x1080")  # Такого размера должно хватить

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')

    guessInput = driver.find_element(By.ID, 'guessInput')
    checkBtn = driver.find_element(By.ID, 'checkBtn')

    for iframe in driver.find_elements(By.TAG_NAME, 'iframe'):
        driver.switch_to.frame(iframe)
        driver.find_element(By.TAG_NAME, 'button').click()
        iframe_text = driver.find_element(By.ID, 'numberDisplay').text
        driver.switch_to.default_content()
        guessInput.clear()
        guessInput.send_keys(iframe_text)
        checkBtn.click()
        try:
            result = driver.switch_to.alert.text
            print(result)
            break
        finally:
            continue