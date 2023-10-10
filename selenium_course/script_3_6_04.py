import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "https://stepik.org/lesson/236895/step/1"

def login(browser_fxtr):

    # Ожидание пропажи лоадера
    WebDriverWait(browser_fxtr, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".stepik-loader")))

    # Клик по Войти
    button = browser_fxtr.find_element(By.CSS_SELECTOR, "#ember35")
    button.click()

    # Ввод логина и пароля
    login = "soulmaxim@gmail.com"
    password = "Slmxm001"
    browser_fxtr.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
    browser_fxtr.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
    browser_fxtr.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()

    # Ожидание пропажи лоадера
    loader = browser_fxtr.find_element(By.CSS_SELECTOR, ".stepik-loader")
    WebDriverWait(browser_fxtr, 30).until(EC.invisibility_of_element(loader))

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898","236899", "236903", "236904", "236905"])
def test_script(browser_fxtr, lesson):

    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser_fxtr.get(link)
    login(browser_fxtr)

    # Вычисление ответа
    answer = math.log(int(time.time()))

    # Проверка того чистый ли textarea
    again_button = browser_fxtr.find_elements(By.CSS_SELECTOR, ".again-btn")
    if len(again_button) > 0:
        again_button[0].click()

    # Проверка того готов ли textarea к вводу
    WebDriverWait(browser_fxtr, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    submit_button = browser_fxtr.find_element(By.CSS_SELECTOR, ".submit-submission")
    WebDriverWait(browser_fxtr, 15).until_not(EC.element_to_be_clickable(submit_button))

    # Ввод ответа
    textarea = browser_fxtr.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(answer)

    # Клик по Отправить
    WebDriverWait(browser_fxtr, 15).until(EC.element_to_be_clickable(submit_button))
    submit_button.click()

    # Получение комментария
    WebDriverWait(browser_fxtr, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    response_text = browser_fxtr.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    assert response_text == 'Correct!'


