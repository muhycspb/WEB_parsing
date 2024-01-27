from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'container')
    for element in elements:
        WebDriverWait(browser, 10).until(EC.element_to_be_selected(element.find_element(By.TAG_NAME, 'input')))
        element.find_element(By.TAG_NAME, 'button').click()
    print(browser.find_element(By.ID, 'result').text)
