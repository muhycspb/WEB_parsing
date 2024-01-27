from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'box_button')
    for element in elements:
        element.click()
        browser.find_element(By.ID, 'close_ad').click()
        WebDriverWait(browser, 20).until(EC.invisibility_of_element((By.ID, 'ad_window')))
        while True:
            if element.text:
                break
    print('-'.join([element.text for element in elements]))
