from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/1/index.html')
    actions = ActionChains(driver)
    element = driver.find_element(By.ID, 'field1')
    container = driver.find_element(By.ID, 'field2')
    actions.drag_and_drop(element, container).perform()
    print(driver.find_element(By.ID, 'result').text)
