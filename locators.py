from selenium.webdriver.common.by import By


# Кнопки формы авторизации и регистрации
LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

# Аватар и имя пользователя 
USER_AVATAR = (By.CSS_SELECTOR, ".circleSmall")
NAME_USER = (By.XPATH, "//h3[contains(@class, 'profileText name')]")

# Поля ввода формы входа и регистрации
EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword']")
   
# Ошибки валидации
LABEL_ERR = (By.XPATH, "//span[text()='Ошибка']")
ERR_FIELD = (By.CSS_SELECTOR, "div.input_inputError__fLUP9")

   
# Создание объявления
BUTTON_CREATE_AD = (By.XPATH, "//button[text()='Разместить объявление']")
TITLE_CREATE_AD = (By.XPATH, "//h1[text()='Новое объявление']")
INPUT_TITLE = (By.XPATH, "//input[@name='name' and @placeholder='Название']")
INPUT_DESCRIPTION = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")  
INPUT_PRICE = (By.XPATH, "//input[@name='price' and @placeholder='Стоимость']") 
BUTTON_PUBLISH = (By.XPATH, "//button[text()='Опубликовать']")
DROPDOWN_CATEGORY = (By.XPATH, "//div[input[@name='category']]//button[contains(@class, 'dropDownMenu_arrowDown') and @type='button']")
SELECT_CATEGORY = (By.XPATH, "//button[span[text()='Садоводство']]")
DROPDOWN_CITY = (By.XPATH, "//div[input[@name='city']]//button[contains(@class, 'dropDownMenu_arrowDown') and @type='button']")
SELECT_CITY = (By.XPATH, "//button[span[text()='Москва']]")
RADIO_CONDITION = (By.CSS_SELECTOR, 'div.radioUnput_shell__Wtdwe input[value="Б/У"] + div.radioUnput_inputRegular__FbVbr')
SECTION_MY_ADS = (By.XPATH, "//h1[text()='Мои объявления']")
ITEM_AD = (By.XPATH, "(//div[contains(@class, 'card')])[last()]")
NOTIFICATION_MODAL = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")