from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input_first_name.send_keys('Qa')
    input_last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input_last_name.send_keys('Testerov')
    input_email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input_email.send_keys('qa@gmail.qa')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(7)
    browser.quit()