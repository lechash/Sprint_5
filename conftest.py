import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from test_data import create_email, create_password, Login_Exist_User, Invalid_email_shows_error, advertisement, MAIN_PAGE_URL
from locators import *

@pytest.fixture
def fresh_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()

@pytest.fixture
def open_main_page(fresh_driver):
    driver, wait = fresh_driver
    driver.get(MAIN_PAGE_URL)
    wait.until(EC.presence_of_element_located(LOGIN_REGISTER_BUTTON))
    yield driver, wait

@pytest.fixture
def registration_form_opened(open_main_page):
    #Фикстура для открытия формы регистрации
    driver, wait = open_main_page
    wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
    yield driver, wait

@pytest.fixture
def submit_registration_form(open_main_page):
    def _submit():
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
    return _submit

@pytest.fixture
def submit_invalid_email_form(registration_form_opened):
    #Фикстура для отправки формы с некорректным email и ожидания элементов ошибки.
    #Возвращает:
   # - driver, wait: драйвер и WebDriverWait
   # - error_msg: элемент с сообщением об ошибке («Ошибка»)
   # - email_field, password_field, confirm_field: поля с красной рамкой (по порядку)
    
    driver, wait = registration_form_opened

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
    # Поскольку ERR_FIELD — общий локатор, получаем все такие элементы
    error_fields = wait.until(EC.presence_of_all_elements_located(ERR_FIELD))

    # Убеждаемся, что найдено минимум 3 поля с ошибкой
    assert len(error_fields) >= 3

    # По порядку: первое поле — Email, второе — Пароль, последнее — Повторите пароль
    email_field = error_fields[0]
    password_field = error_fields[1]
    confirm_field = error_fields[-1]  # последний элемент

    return driver, wait, error_msg, email_field, password_field, confirm_field

@pytest.fixture
def submit_existing_user_form(registration_form_opened):
    #Фикстура для отправки формы с данными существующего пользователя
    driver, wait = registration_form_opened
    driver.find_element(*EMAIL_INPUT).send_keys(Login_Exist_User.exist_user_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
    driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
    create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    create_button.click()
    try:
        error_msg = wait.until(EC.visibility_of_element_located(LABEL_ERR))
    except:
        error_msg = None
    email_field = driver.find_element(*EMAIL_INPUT)
    password_field = driver.find_element(*PASSWORD_INPUT)
    confirm_field = driver.find_element(*CONFIRM_PASSWORD_INPUT)
    return driver, wait, error_msg, email_field, password_field, confirm_field

@pytest.fixture
def login_assertion():
    def _assert_login(login_successful):
        assert login_successful, "Авторизация не удалась — тест не может быть выполнен"
    return _assert_login

@pytest.fixture
def user_logged_in(open_main_page):
    #Фикстура для авторизации пользователя. Возвращает (driver, wait, login_successful)
    driver, wait = open_main_page
    login_successful = False

    try:
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

    except TimeoutException:
        print("Авторизация не удалась: элемент имени пользователя не появился.")

    return driver, wait, login_successful

@pytest.fixture
def logout_performed(user_logged_in):
    #Фикстура для выполнения выхода из системы. Выполняется только если авторизация прошла успешно
    driver, wait, login_successful = user_logged_in

    if not login_successful:
        pytest.fail("Авторизация не удалась — невозможно выполнить выход из системы")

    # Выполняем выход
    logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # Ждём перезагрузки страницы
    wait.until(EC.url_contains(MAIN_PAGE_URL))
    yield driver, wait

@pytest.fixture
def ad_creation_form_opened(user_logged_in):
    # Фикстура для открытия формы создания объявления, пользователь авторизован.
       
    driver, wait, login_successful = user_logged_in

    if not login_successful:
        return driver, wait, False  # Возвращаем флаг неудачи

    try:
        create_ad_button = wait.until(EC.element_to_be_clickable(BUTTON_CREATE_AD))
        create_ad_button.location_once_scrolled_into_view
        create_ad_button.click()
        wait.until(EC.visibility_of_element_located(INPUT_TITLE))
        return driver, wait, True  # Успех
    except Exception as e:
        print(f"Не удалось открыть форму создания объявления: {e}")
        return driver, wait, False  # Неудача

@pytest.fixture
def modal_window_appeared(fresh_driver):
    #Фикстура: открывает главную страницу и нажимает «Разместить объявление» для неавторизованного пользователя
    driver, wait = fresh_driver
    driver.get(MAIN_PAGE_URL)
    wait.until(EC.presence_of_element_located(BUTTON_CREATE_AD))

    create_ad_button = wait.until(EC.element_to_be_clickable(BUTTON_CREATE_AD))
    create_ad_button.click()

    modal_window = wait.until(EC.visibility_of_element_located(NOTIFICATION_MODAL))
    yield modal_window

@pytest.fixture
def registered_user_with_ad_form(open_main_page):
    driver, wait = open_main_page

    # Шаг 1: регистрация нового пользователя
    login_register_btn = wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON))
    login_register_btn.click()

    no_account_btn = wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON))
    no_account_btn.click()

    email = create_email()
    password = create_password()

    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)

    create_button = wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON))
    create_button.click()

    # Ждём подтверждения регистрации (аватар)
    wait.until(EC.visibility_of_element_located(USER_AVATAR))

    # Шаг 2: открытие формы создания объявления
    create_ad_btn = wait.until(EC.element_to_be_clickable(BUTTON_CREATE_AD))
    create_ad_btn.click()

    # Проверяем появление заголовка формы вместо имени пользователя
    try:
        wait.until(EC.visibility_of_element_located(TITLE_CREATE_AD))
        # Дополнительно ждём доступности первого поля ввода
        wait.until(EC.element_to_be_clickable(INPUT_TITLE))
        form_opened = True
    except:
        form_opened = False

    yield driver, wait, email, password, form_opened

