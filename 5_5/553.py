from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    for field in browser.find_elements(By.CLASS_NAME, 'text-field'):
        field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
