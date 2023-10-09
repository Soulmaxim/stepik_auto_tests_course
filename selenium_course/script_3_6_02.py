from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser_fxtr):
    browser_fxtr.get(link)
    browser_fxtr.find_element(By.CSS_SELECTOR, "#login_link")