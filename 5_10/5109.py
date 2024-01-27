import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/2/index.html')
    time.sleep(1)
    targets = driver.find_elements(By.CLASS_NAME, 'box')
    block = driver.find_element(By.ID, 'draggable')
    for target in targets:
        ActionChains(driver).drag_and_drop(block, target).perform()
        time.sleep(1)
    time.sleep(5)
    print(driver.find_element(By.ID, 'message').text)
