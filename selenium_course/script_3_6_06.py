import time

from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://stepik.org/lesson/25969/step/8")
driver.fullscreen_window()
time.sleep(5)
driver.quit()
