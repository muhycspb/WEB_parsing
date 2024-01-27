import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/4/index.html')
    time.sleep(1)
    baskets = driver.find_elements(By.CLASS_NAME, 'basket_color')
    balls = driver.find_elements(By.CLASS_NAME, 'ball_color')
    for basket in baskets:
        for ball in balls:
            ball_color = ball.value_of_css_property('background-color')
            basket_color = basket.value_of_css_property('background-color')
            if ball_color == basket_color:
                ActionChains(driver).drag_and_drop(ball, basket).perform()
        time.sleep(1)
    time.sleep(5)
    print(driver.find_element(By.CLASS_NAME, 'message').text)
