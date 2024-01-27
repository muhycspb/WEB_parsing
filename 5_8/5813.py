from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html', 'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html', ]

with webdriver.Chrome() as driver:
    for i, site in enumerate(sites, 1):
        driver.execute_script(f'window.open("{site}", "_blank{i}");')
    result = 0
    for x in range(len(driver.window_handles)):
        driver.switch_to.window(driver.window_handles[x])
        for y in driver.find_elements(By.CLASS_NAME, 'check_box'):
            y.click()
            result += int(driver.find_element(By.ID, 'result').text) ** 0.5
print(round(result, 9))
