from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    print('Window handles 1:', browser.window_handles)
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    print('Window handles 2:', browser.window_handles)
    # time.sleep(3)
    button.click()
    print('Window handles 3:', browser.window_handles)
    print('Current window', browser.current_window_handle)
    browser.switch_to.window(browser.window_handles[1])
    print('Current window', browser.current_window_handle)

    x = browser.find_element(By.ID, 'input_value').text
    solve = calc(x)
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(solve)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # time.sleep(7)
    browser.quit()

