from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    main_container = browser.find_elements(By.ID, 'main-container')[-1]
    for div in main_container.find_elements(By.XPATH, 'div'):
        span = div.find_element(By.XPATH, 'span').text
        div.find_element(By.CSS_SELECTOR, f'select option[value="{span}"]').click()
        div.find_element(By.CSS_SELECTOR, f'div button[data-hex="{span}"]').click()
        div.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        div.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(span)
        div.find_element(By.XPATH, 'button').click()

    browser.find_elements(By.CSS_SELECTOR, 'button')[-1].click()
    print(browser.switch_to.alert.text)
    time.sleep(5)