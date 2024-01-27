from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    browser.find_element(By.LINK_TEXT, '16243162441624').click()
    print(browser.find_element(By.ID, 'result').text)
