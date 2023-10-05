from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def passCapcha(browser):
    x = browser.find_element(By.ID, 'input_value').text
    solve = calc(x)
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(solve)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    solve = calc(x)
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(solve)
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
