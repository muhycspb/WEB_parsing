import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/3/index.html')
    time.sleep(1)
    frames = driver.find_elements(By.CLASS_NAME, 'draganddrop_end')
    blocks = driver.find_elements(By.CLASS_NAME, 'draganddrop')
    for block in blocks:
        for frame in frames:
            block_color = ''.join([i for i in block.value_of_css_property('background-color') if i.isdigit() or i == ','])[:-2]
            frame_color = ''.join([i for i in frame.value_of_css_property('border-color') if i.isdigit() or i == ','])
            if block_color == frame_color:
                ActionChains(driver).drag_and_drop(block, frame).perform()
        time.sleep(1)
    time.sleep(5)
    print(driver.find_element(By.ID, 'message').text)
