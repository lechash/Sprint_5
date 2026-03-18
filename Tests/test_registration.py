import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data import Login_Exist_User, MAIN_PAGE_URL
from locators import *
from helpers import *

class TestRegistrationValidData:
    def test_successful_registration_redirect(self, open_main_page):
        #Тест: произошёл переход на главную страницу после регистрации
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Шаг 3: Заполнить форму и отправить
        email = create_email()
        password = create_password()

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)

        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        assert driver.current_url.startswith(MAIN_PAGE_URL)

    def test_user_avatar_displayed(self, open_main_page):
        #Тест: отображается аватар пользователя после регистрации
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Шаг 3: Заполнить форму и отправить
        email = create_email()
        password = create_password()

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)

        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Явно ждём появления аватара пользователя
        avatar = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        assert avatar.is_displayed()
        
    def test_user_name_contains_user(self, open_main_page):
        #Тест: имя пользователя содержит 'User' после регистрации
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Шаг 3: Заполнить форму и отправить
        email = create_email()
        password = create_password()

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)

        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Явно ждём появления имени пользователя
        user_name_element = wait.until(EC.visibility_of_element_located(NAME_USER))
        user_name_text = user_name_element.text
        assert 'User' in user_name_text

class TestRegistrationWithInvalidEmail:

    def test_error_message_displayed_under_email(self, open_main_page):
    # Проверка, что под полем Email отображается сообщение «Ошибка»
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Заполняем форму некорректными данными
        email = "invalid_email"  # намеренно некорректный email
        password = create_password()

        email_input = driver.find_element(*EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = driver.find_element(*PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = driver.find_element(*CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Ждём появления сообщения об ошибке
        error_msg = wait.until(EC.visibility_of_element_located(LABEL_ERR))
       
        assert error_msg.text == "Ошибка"

    def test_email_field_highlighted_red(self, open_main_page):
        #  Проверяет, что поле Email выделено красным (цвет rgb(255, 105, 114))
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Заполняем форму некорректными данными
        email = "invalid_email"  # намеренно некорректный email
        password = create_password()

        email_input = driver.find_element(*EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = driver.find_element(*PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = driver.find_element(*CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Ждём, пока появятся все поля с ошибкой (красная рамка)
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

        # Ждём появления полей с ошибкой
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

        # Поле Email — первое в списке полей с ошибкой
        email_error_field = error_fields[0]

        # Получаем цвет границы элемента
        border_color = email_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля Email соответствует ожидаемому
        assert border_color == expected_color

    def test_password_field_highlighted_red(self, open_main_page):
        # Проверяет, что поле «Пароль» выделено красным (цвет rgb(255, 105, 114))
        
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Заполняем форму некорректными данными
        email = "invalid_email"  # намеренно некорректный email
        password = create_password()

        email_input = driver.find_element(*EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = driver.find_element(*PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = driver.find_element(*CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Ждём появления полей с ошибкой
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

        # Поле «Пароль» — второе в списке полей с ошибкой
        password_error_field = error_fields[1]

        # Получаем цвет границы элемента
        border_color = password_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Пароль» соответствует ожидаемому
        assert border_color == expected_color

    def test_confirm_password_field_highlighted_red(self, open_main_page):
        # Проверяет, что поле «Повторите пароль» выделено красным (цвет rgb(255, 105, 114))
        
        driver, wait = open_main_page

        # Шаг 1: Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Шаг 2: Нажать «Нет аккаунта»
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        # Заполняем форму некорректными данными
        email = "invalid_email"  # намеренно некорректный email
        password = create_password()

        email_input = driver.find_element(*EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = driver.find_element(*PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = driver.find_element(*CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()
       
        # Ждём появления полей с ошибкой
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

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

    def test_error_message_displayed_under_email_field(self, open_main_page):
        #Тест: проверить, что под полем Email отображается сообщение «Ошибка»
        driver, wait = open_main_page

        # Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Нажать «Нет аккаунта» и заполнить форму
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        driver.find_element(*EMAIL_INPUT).send_keys(Login_Exist_User.exist_user_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Ждём появления сообщения об ошибке
        error_msg = wait.until(EC.visibility_of_element_located(LABEL_ERR))
      
        # Проверяем, что элемент с сообщением «Ошибка» виден на странице
        assert error_msg.text == "Ошибка"

    def test_email_field_highlighted_in_red_with_correct_color(self, open_main_page):
        #Тест: проверить, что поле Email выделено красным цветом (rgb(255, 105, 114))
        
        driver, wait = open_main_page

        # Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Нажать «Нет аккаунта» и заполнить форму
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        driver.find_element(*EMAIL_INPUT).send_keys(Login_Exist_User.exist_user_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Ждём появления полей с ошибкой
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

        # Поле Email — первое в списке полей с ошибкой
        email_error_field = error_fields[0]

        # Получаем цвет границы элемента
        border_color = email_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля Email соответствует ожидаемому
        assert border_color == expected_color

    def test_password_field_highlighted_in_red_with_correct_color(self, open_main_page):
       #Тест: проверить, что поле «Пароль» выделено красным цветом (rgb(255, 105, 114))
        
        driver, wait = open_main_page

        # Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Нажать «Нет аккаунта» и заполнить форму
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        driver.find_element(*EMAIL_INPUT).send_keys(Login_Exist_User.exist_user_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()

        # Ждём появления полей с ошибкой
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

        # Поле «Пароль» — второе в списке полей с ошибкой
        password_error_field = error_fields[1]

        # Получаем цвет границы элемента
        border_color = password_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Пароль» соответствует ожидаемому
        assert border_color == expected_color

    def test_confirm_password_field_highlighted_in_red_with_correct_color(self, open_main_page):
        #Тест: проверить, что поле «Повторите пароль» выделено красным цветом (rgb(255, 105, 114))
    
        driver, wait = open_main_page

        # Нажать «Вход и регистрация»
        login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
        login_register_btn.click()

        # Нажать «Нет аккаунта» и заполнить форму
        no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
        no_account_btn.click()

        driver.find_element(*EMAIL_INPUT).send_keys(Login_Exist_User.exist_user_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)

        # Отправляем форму
        create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
        create_button.click()
        
        # Ждём появления полей с ошибкой
        error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

        # Поле «Повторите пароль» — последнее в списке полей с ошибкой
        confirm_error_field = error_fields[-1]

        # Получаем цвет границы элемента
        border_color = confirm_error_field.value_of_css_property("border-color")

        # Ожидаемый цвет в формате RGB
        expected_color = "rgb(255, 105, 114)"

        # Убеждаемся, что цвет границы поля «Повторите пароль» соответствует ожидаемому
        assert border_color == expected_color
        