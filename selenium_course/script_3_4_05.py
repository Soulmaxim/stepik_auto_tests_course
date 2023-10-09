import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser_fixture():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser_fixture):
        print("start test1")
        browser_fixture.get(link)
        time.sleep(3)
        browser_fixture.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser_fixture):
        print("start test2")
        browser_fixture.get(link)
        time.sleep(3)
        browser_fixture.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
