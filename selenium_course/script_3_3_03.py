from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    browser = webdriver.Chrome()
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        input_first_name = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input_first_name.send_keys('Qa')
        input_last_name = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input_last_name.send_keys('Testerov')
        input_email = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input_email.send_keys('qa@gmail.qa')

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        input_first_name = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your name"]')
        input_first_name.send_keys('Qa')
        input_last_name = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input_last_name.send_keys('Testerov')
        input_email = self.browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input_email.send_keys('qa@gmail.qa')

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
