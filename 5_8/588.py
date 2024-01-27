import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/1/')
    driver.set_window_size(568, 691)
    print(driver.find_element(By.ID, 'width').text)
    print(driver.find_element(By.ID, 'height').text)
    print(driver.find_element(By.ID, 'result').text)
    time.sleep(10)