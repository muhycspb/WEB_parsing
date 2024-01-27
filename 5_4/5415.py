from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

data = []

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    for i in browser.find_elements(By.TAG_NAME, 'option'):
        data.append(int(i.text))
    browser.find_element(By.ID, 'input_result').send_keys(sum(data))
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)