from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    res = str(eval(browser.find_element(By.ID, 'text_box').text))
    for i in browser.find_elements(By.TAG_NAME, 'option'):
        if i.text == res:
            i.click()
            break
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)
