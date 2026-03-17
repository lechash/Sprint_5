import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from test_data import create_email, create_password, Login_Exist_User, Invalid_email_shows_error, advertisement, MAIN_PAGE_URL
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
def submit_registration_form(open_main_page):
    
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

    return driver, wait, email, password

@pytest.fixture
def submit_invalid_email_form(open_main_page):
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

    # Ждём, пока появятся все поля с ошибкой (красная рамка)
    error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

    # По порядку: первое поле — Email, второе — Пароль, последнее — Повторите пароль
    email_field = error_fields[0]
    password_field = error_fields[1]
    confirm_field = error_fields[-1]  # последний элемент

    return driver, wait, error_msg, email_field, password_field, confirm_field

@pytest.fixture
def submit_existing_user_form(open_main_page):
    driver, wait = open_main_page

    # Шаг 1: Нажать «Вход и регистрация»
    login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
    login_register_btn.click()

    # Шаг 2: Нажать «Нет аккаунта»
    no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
    no_account_btn.click()

    # Шаг 3: Заполнить данными ранее зарегистрированного юзера
    driver.find_element(*EMAIL_INPUT).send_keys(Login_Exist_User.exist_user_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
    driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)

    create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    create_button.click()
    error_msg = wait.until(EC.visibility_of_element_located(LABEL_ERR))
    email_field = driver.find_element(*EMAIL_INPUT)
    password_field = driver.find_element(*PASSWORD_INPUT)
    confirm_field = driver.find_element(*CONFIRM_PASSWORD_INPUT)

    return driver, wait, error_msg, email_field, password_field, confirm_field


@pytest.fixture
def user_logged_in(open_main_page):
    #Фикстура для авторизации пользователя
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
