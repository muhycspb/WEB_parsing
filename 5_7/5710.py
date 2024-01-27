from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/scroll/2/index.html')

    items = driver.find_elements(By.CLASS_NAME, 'item')
    actions = ActionChains(driver)

    total = 0

    for item in items:
        checkbox = item.find_element(By.CLASS_NAME, 'checkbox_class')
        actions.move_to_element(checkbox).perform()
        checkbox.click()
        span = item.find_element(By.TAG_NAME, 'span').text
        if span:
            total += int(span)

    print(total)