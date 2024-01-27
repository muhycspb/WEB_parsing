from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/window_size/2/index.html')

    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    for x, y in product(window_size_x, window_size_y):
        driver.set_window_size(x + 16, y + 138)
        result = driver.find_element(By.ID, 'result').text
        if result:
            print(x, y)
            break
