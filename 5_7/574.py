from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    total = 0
    elements = browser.find_elements(By.CLASS_NAME, 'btn')
    for element in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        total += int(browser.find_element(By.ID, 'result').text)
    print(total)
