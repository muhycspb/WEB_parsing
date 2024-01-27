import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/3/index.html')

    for page in driver.find_elements(By.TAG_NAME, 'input'):
        page.click()
        time.sleep(.3)

    total = 0

    for n in range(1, len(driver.window_handles)):
        driver.switch_to.window(driver.window_handles[n])
        total += int(driver.execute_script('return document.title;'))
        time.sleep(.5)

    print(total)

    time.sleep(10)
