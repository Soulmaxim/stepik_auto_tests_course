import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_pass(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
