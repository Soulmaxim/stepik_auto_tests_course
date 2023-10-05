from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.NAME, 'firstname')
    first_name_input.send_keys('Ivan')
    last_name_input = browser.find_element(By.NAME, 'lastname')
    last_name_input.send_keys('Ivanov')
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('qa@gmail.qa')
    download_file_input = browser.find_element(By.NAME, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(__file__)
    print(current_dir)
    print(os.path.abspath(__file__))
    print(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    download_file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()