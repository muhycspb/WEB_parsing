import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/8/index.html')
    time.sleep(1)
    ranges = driver.find_elements(By.CLASS_NAME, 'range')
    pieces = driver.find_elements(By.CLASS_NAME, 'piece')
    for rang in ranges:
        for piece in pieces:
            piece_color = piece.value_of_css_property('background-color')
            rang_color = rang.value_of_css_property('background-color')
            if piece_color == rang_color:
                ActionChains(driver).drag_and_drop(piece, rang).perform()
        time.sleep(1)
    time.sleep(5)
    print(driver.find_element(By.ID, 'message').text)
