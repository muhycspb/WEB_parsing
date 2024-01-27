from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://parsinger.ru/selenium/5.7/5/index.html')

buttons = driver.find_elements(By.CLASS_NAME, 'timer_button')
actions = ActionChains(driver)

for button in buttons:
    actions.click_and_hold(button).pause(float(button.get_attribute('value'))).release(button).perform()

print(driver.switch_to.alert.text)
