from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_1/')

    list_input = []
    while len(list_input) != 100:

        input_tags = driver.find_elements(By.CSS_SELECTOR, '#scroll-container input')

        for tag_input in input_tags:
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)
                driver.execute_script('return arguments[0].scrollIntoView(true);', tag_input)
                list_input.append(tag_input)

    print(sum([int(i.text) for i in driver.find_elements(By.CSS_SELECTOR, '#scroll-container span')]))
