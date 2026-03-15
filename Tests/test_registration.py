import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data import Login_Exist_User, MAIN_PAGE_URL
from locators import *

class TestRegistrationValidData:
    def test_successful_registration_redirect(self, submit_registration_form):
        #Тест: произошёл переход на главную страницу после регистрации
        driver, wait, email, password = submit_registration_form()
        assert driver.current_url.startswith(MAIN_PAGE_URL)

    def test_user_avatar_displayed(self, submit_registration_form):
        #Тест: отображается аватар пользователя после регистрации
        driver, wait, email, password = submit_registration_form()

        # Явно ждём появления аватара пользователя
        avatar = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        assert avatar.is_displayed()
        
    def test_user_name_contains_user(self, submit_registration_form):
        #Тест: имя пользователя содержит 'User' после регистрации
        driver, wait, email, password = submit_registration_form()

        # Явно ждём появления имени пользователя
        user_name_element = wait.until(EC.visibility_of_element_located(NAME_USER))
        user_name_text = user_name_element.text
        assert 'User' in user_name_text

class TestRegistrationWithInvalidEmail:
    @pytest.fixture(autouse=True)
    def setup(self, submit_invalid_email_form):
        self.driver, self.wait, self.error_msg, self.email_field, self.password_field, self.confirm_field = submit_invalid_email_form

    def test_error_message_displayed_under_email(self):
       #Проверка, что под полем Email отображается сообщение «Ошибка»
        error_text = self.error_msg.text
        assert error_text == "Ошибка"

    def test_email_field_highlighted_red(self, submit_invalid_email_form):
        #  Проверяет, что поле Email выделено красным (цвет rgb(255, 105, 114))
        
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_invalid_email_form
        # Получаем все поля с красной рамкой
        error_fields = driver.find_elements(*ERR_FIELD)

        # Поле Email — первое в списке полей с ошибкой
        email_error_field = error_fields[0]

        # Получаем цвет границы элемента
        border_color = email_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля Email соответствует ожидаемому
        assert border_color == expected_color

    def test_password_field_highlighted_red(self, submit_invalid_email_form):
        # Проверяет, что поле «Пароль» выделено красным (цвет rgb(255, 105, 114))
        
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_invalid_email_form
        # Получаем все поля с красной рамкой
        error_fields = driver.find_elements(*ERR_FIELD)

        # Поле «Пароль» — второе в списке полей с ошибкой
        password_error_field = error_fields[1]

        # Получаем цвет границы элемента
        border_color = password_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Пароль» соответствует ожидаемому
        assert border_color == expected_color

    def test_confirm_password_field_highlighted_red(self, submit_invalid_email_form):
        # Проверяет, что поле «Повторите пароль» выделено красным (цвет rgb(255, 105, 114))
        
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_invalid_email_form
        # Получаем все поля с красной рамкой
        error_fields = driver.find_elements(*ERR_FIELD)

        # Поле «Повторите пароль» — последнее в списке полей с ошибкой
        confirm_error_field = error_fields[-1]

        # Получаем цвет границы элемента
        border_color = confirm_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Повторите пароль» соответствует ожидаемому
        assert border_color == expected_color

class TestRegistrationExistingUser:
    #Тесты для сценария регистрации уже существующего пользователя с проверкой цвета выделения полей

    def test_error_message_displayed_under_email_field(self, submit_existing_user_form):
        #Тест: проверить, что под полем Email отображается сообщение «Ошибка»
        
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_existing_user_form

        # Проверяем, что элемент с сообщением «Ошибка» виден на странице
        assert error_msg.text == "Ошибка"

    def test_email_field_highlighted_in_red_with_correct_color(self, submit_existing_user_form):
        #Тест: проверить, что поле Email выделено красным цветом (rgb(255, 105, 114))
        
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_existing_user_form

        # Получаем все поля с красной рамкой
        error_fields = driver.find_elements(*ERR_FIELD)

        # Поле Email — первое в списке полей с ошибкой
        email_error_field = error_fields[0]

        # Получаем цвет границы элемента
        border_color = email_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля Email соответствует ожидаемому
        assert border_color == expected_color

    def test_password_field_highlighted_in_red_with_correct_color(self, submit_existing_user_form):
       #Тест: проверить, что поле «Пароль» выделено красным цветом (rgb(255, 105, 114))
        
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_existing_user_form

        # Получаем все поля с красной рамкой
        error_fields = driver.find_elements(*ERR_FIELD)

        # Поле «Пароль» — второе в списке полей с ошибкой
        password_error_field = error_fields[1]

        # Получаем цвет границы элемента
        border_color = password_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Пароль» соответствует ожидаемому
        assert border_color == expected_color

    def test_confirm_password_field_highlighted_in_red_with_correct_color(self, submit_existing_user_form):
        #Тест: проверить, что поле «Повторите пароль» выделено красным цветом (rgb(255, 105, 114))
    
        driver, wait, error_msg, email_field, password_field, confirm_field = submit_existing_user_form

        # Получаем все поля с красной рамкой
        error_fields = driver.find_elements(*ERR_FIELD)

        # Поле «Повторите пароль» — последнее в списке полей с ошибкой
        confirm_error_field = error_fields[-1]

        # Получаем цвет границы элемента
        border_color = confirm_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Повторите пароль» соответствует ожидаемому
        assert border_color == expected_color
        