from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_2/')

    list_p = []
    while len(list_p) != 100:

        p_tags = driver.find_elements(By.CSS_SELECTOR, '#scroll-container p')

        for tag_p in p_tags:
            if tag_p not in list_p:
                ActionChains(driver).scroll_to_element(tag_p).perform()
                driver.execute_script('return arguments[0].scrollIntoView(true);', tag_p)
                list_p.append(tag_p)

    print(sum([int(i.text) for i in list_p]))
