from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'button-container')
    for element in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
    print(browser.switch_to.alert.text)