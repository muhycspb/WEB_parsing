from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    for id_ in ids_to_find:
        WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, id_)))
        browser.find_element(By.ID, id_).click()
    print(browser.switch_to.alert.text)