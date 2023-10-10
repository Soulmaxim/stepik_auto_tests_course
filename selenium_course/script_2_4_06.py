from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/cats.html?'
    browser = webdriver.Chrome()
    browser.get(link)

    answer_input = browser.find_element(By.ID, 'button')

finally:
    time.sleep(6)
    browser.quit()
