import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/3/index.html')
    actions = ActionChains(driver)
    points = driver.find_elements(By.CLASS_NAME, 'controlPoint')
    block = driver.find_element(By.ID, 'block1')
    actions.click_and_hold(block)
    for point in points:
        time.sleep(1)
        actions.move_to_element(point)
    actions.perform()
    time.sleep(5)
    print(driver.find_element(By.ID, 'message').text)
