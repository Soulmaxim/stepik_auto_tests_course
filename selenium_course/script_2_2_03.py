from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1Element = browser.find_element(By.ID, 'num1')
    num1 = int(num1Element.text)
    num2Element = browser.find_element(By.ID, 'num2')
    num2 = int(num2Element.text)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(num1+num2))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()