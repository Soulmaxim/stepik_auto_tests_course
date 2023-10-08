import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def wut():
    print("\nstart browser for test..")
    wuta = webdriver.Chrome()
    yield wuta
    print("\nquit browser..")
    wuta.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, wut):
        print("start test1")
        wut.get(link)
        time.sleep(5)
        wut.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, wut):
        print("start test2")
        wut.get(link)
        time.sleep(5)
        wut.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
