from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    for i in browser.find_elements(By.CLASS_NAME, 'parent'):
        gray = i.find_element(By.XPATH, '*[1]')
        blue = i.find_element(By.XPATH, '*[2]')
        blue.send_keys(gray.text)
        gray.clear()
        i.find_element(By.XPATH, '*[3]').click()
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)