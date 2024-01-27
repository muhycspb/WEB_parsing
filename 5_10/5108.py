import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/2/index.html')
    time.sleep(1)
    blocks = driver.find_elements(By.CLASS_NAME, 'draganddrop')
    target = driver.find_element(By.CLASS_NAME, 'draganddrop_end')
    for block in blocks:
        ActionChains(driver).drag_and_drop(block, target).perform()
        time.sleep(1)
    time.sleep(5)
    print(driver.find_element(By.ID, 'message').text)
