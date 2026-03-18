import pytest
from test_data import Login_Exist_User, MAIN_PAGE_URL
from locators import *
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_login_redirects_to_main_page(self, open_main_page):
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
        
        assert driver.current_url.startswith(MAIN_PAGE_URL)

    def test_login_displays_user_avatar(self, open_main_page):
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

        avatar = wait.until(EC.visibility_of_element_located(USER_AVATAR))

        assert avatar.is_displayed()

    def test_login_displays_user_name_with_user_text(self, open_main_page):
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

        user_name_element = wait.until(EC.visibility_of_element_located(NAME_USER))
        user_name_text = user_name_element.text
        assert "User" in user_name_text