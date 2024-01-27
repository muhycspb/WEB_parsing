from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    browser.find_element(By.CLASS_NAME, 'close').click()
    WebDriverWait(browser, 100).until(EC.invisibility_of_element_located((By.ID, 'ad')))
    browser.find_element(By.CLASS_NAME, 'box').click()
    print(browser.find_element(By.ID, 'message').text)


