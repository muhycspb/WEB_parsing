from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    locator = (By.CLASS_NAME, 'BMH21YY')
    if WebDriverWait(browser, poll_frequency=0.5, timeout=40).until(EC.presence_of_element_located(locator)):
        print(browser.find_element(*locator).text)
