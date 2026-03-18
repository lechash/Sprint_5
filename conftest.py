import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data import *
from locators import *

@pytest.fixture
def open_main_page():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(MAIN_PAGE_URL)
    wait.until(EC.presence_of_element_located(LOGIN_REGISTER_BUTTON))
    yield driver, wait
    driver.quit()

@pytest.fixture
def user_logged_in(open_main_page):
    #Фикстура для авторизации пользователя. Возвращает (driver, wait, login_successful)
    driver, wait = open_main_page

        # Открываем форму авторизации
    login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
    login_register_btn.click()

        # Заполняем поле email
    email_input = wait.until(EC.presence_of_element_located(EMAIL_INPUT))
    email_input.send_keys(Login_Exist_User.exist_user_mail)

        # Заполняем поле пароля
    password_input = wait.until(EC.presence_of_element_located(PASSWORD_INPUT))
    password_input.send_keys(Login_Exist_User.exist_user_pass)

        # Нажимаем «Войти»
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

        # Ждём появления элемента имени пользователя (маркер успешной авторизации)
    wait.until(EC.visibility_of_element_located(NAME_USER))
    login_successful = True

    return driver, wait, login_successful
