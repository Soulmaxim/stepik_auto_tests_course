from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    solve = calc(x)
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(solve)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()