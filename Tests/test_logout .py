import pytest
from selenium.webdriver.support import expected_conditions as EC
from test_data import MAIN_PAGE_URL
from locators import *

class TestLogout:
    def test_logout_hides_user_avatar(self, user_logged_in, login_assertion):
        #Тест: аватар пользователя скрывается после выхода
        driver, wait, login_successful = user_logged_in
        login_assertion(login_successful)

        # Выполняем выход
        logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        wait.until(EC.url_contains(MAIN_PAGE_URL))

        # Основной ассерт: ждём исчезновения и явно проверяем отсутствие
        wait.until(EC.invisibility_of_element_located(USER_AVATAR))
        assert not driver.find_elements(*USER_AVATAR)

    def test_logout_hides_user_name(self, user_logged_in, login_assertion):
        #Тест: имя пользователя скрывается после выхода
        driver, wait, login_successful = user_logged_in
        login_assertion(login_successful)

        # Выполняем выход
        logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        wait.until(EC.url_contains(MAIN_PAGE_URL))

        # Основной ассерт: ждём исчезновения и явно проверяем отсутствие
        wait.until(EC.invisibility_of_element_located(NAME_USER))
        assert not driver.find_elements(*NAME_USER)

    def test_logout_displays_login_button(self, user_logged_in, login_assertion):
        #Тест: кнопка «Вход и регистрация» отображается после выхода
        driver, wait, login_successful = user_logged_in
        login_assertion(login_successful)

        # Выполняем выход
        logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        wait.until(EC.url_contains(MAIN_PAGE_URL))

        # Основной ассерт
        login_button = wait.until(EC.visibility_of_element_located(LOGIN_REGISTER_BUTTON))
        assert login_button.is_displayed()


class TestLogoutWithRegiastration:
    def test_logout_hides_user_avatar_with_registration(self, submit_registration_form):
        #Тест: аватар пользователя скрывается после выхода
        # Шаг 1: регистрация нового пользователя
        driver, wait, email, password = submit_registration_form()

        # Шаг 2: выход из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        wait.until(EC.url_contains(MAIN_PAGE_URL))

        # Основной ассерт: ждём исчезновения и явно проверяем отсутствие
        wait.until(EC.invisibility_of_element_located(USER_AVATAR))
        assert not driver.find_elements(*USER_AVATAR)

    def test_logout_hides_user_name_with_registration(self, submit_registration_form):
        #Тест: имя пользователя скрывается после выхода
        # Шаг 1: регистрация нового пользователя
        driver, wait, email, password = submit_registration_form()

        # Шаг 2: выход из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        wait.until(EC.url_contains(MAIN_PAGE_URL))

        # Основной ассерт: ждём исчезновения и явно проверяем отсутствие
        wait.until(EC.invisibility_of_element_located(NAME_USER))
        assert not driver.find_elements(*NAME_USER)

    def test_logout_displays_login_button_with_registration(self, submit_registration_form):
        #Тест: кнопка «Вход и регистрация» отображается после выхода
        # Шаг 1: регистрация нового пользователя
        driver, wait, email, password = submit_registration_form()

        # Шаг 2: выход из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        wait.until(EC.url_contains(MAIN_PAGE_URL))

        # Основной ассерт
        login_button = wait.until(EC.visibility_of_element_located(LOGIN_REGISTER_BUTTON))
        assert login_button.is_displayed()
        