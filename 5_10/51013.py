import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/6/index.html')
    time.sleep(1)
    sliders = driver.find_elements(By.CLASS_NAME, 'slider-container')
    actions = ActionChains(driver)
    for slider in sliders:
        target = int(slider.find_element(By.CLASS_NAME, 'target-value').text)
        slider.click()
        while True:
            current = int(slider.find_element(By.CLASS_NAME, 'current-value').text)
            if current < target:
                actions.send_keys(Keys.ARROW_RIGHT)
            elif current > target:
                actions.send_keys(Keys.ARROW_LEFT)
            actions.perform()
            time.sleep(0.1)
            if current == target:
                break

    print(driver.find_element(By.ID, 'message').text)
