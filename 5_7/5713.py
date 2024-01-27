from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_3/')

    list_span = []
    total = 0

    for i in range(1, 6):
        while len(list_span) != 100:
            span_tags = driver.find_elements(By.CSS_SELECTOR, f'#scroll-container_{i} span')

            for tag_span in span_tags:
                if tag_span not in list_span:
                    ActionChains(driver).scroll_to_element(tag_span).perform()
                    driver.execute_script('return arguments[0].scrollIntoView(true);', tag_span)
                    list_span.append(tag_span)

        total += sum([int(i.text) for i in list_span])
        list_span.clear()

    print(total)