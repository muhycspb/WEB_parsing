from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as webdriver:
    data ={}
    webdriver.get('https://parsinger.ru/methods/5/index.html')
    for a in webdriver.find_elements(By.TAG_NAME, 'a'):
        a.click()
        data[f'{webdriver.get_cookie('foo2')['expiry']}'] = webdriver.find_element(By.ID, 'result').text
        webdriver.back()
    print(data[max(data)])