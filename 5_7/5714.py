import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')

    list_containers = []

    while len(list_containers) != 100:
        child_containers = driver.find_elements(By.CSS_SELECTOR, '#main_container .child_container')

        for container in child_containers:
            if container not in list_containers:
                for input_tag in container.find_elements(By.CSS_SELECTOR, 'input'):
                    if int(input_tag.get_attribute('value')) % 2 == 0:
                        input_tag.click()
                ActionChains(driver).scroll_to_element(container).perform()
                driver.execute_script('return arguments[0].scrollIntoView(true);', container)
                list_containers.append(container)
    driver.find_element(By.CSS_SELECTOR, '.alert_button').click()
    print(driver.switch_to.alert.text)
