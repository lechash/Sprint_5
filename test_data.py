from selenium.webdriver.support.ui import WebDriverWait
import random
from faker import Faker

# Генераторы данных
def create_email():
    fake = Faker()
    return fake.email()

def create_password():
    fake = Faker()
    return fake.password(length=10)

def get_wait(driver):
    return WebDriverWait(driver, 15)


# Заготовленные данные
class Login_Exist_User:
    exist_user_mail = '12345654321@ya.ru'
    exist_user_pass = '12345654322'

class Invalid_email_shows_error:
    invalid_mail = "invalid_email"
    password = "Password"

class advertisement:
    product_name = 'Тестовый товар для продажи'
    description = 'Продаю за дорого'
    price = 1000000

MAIN_PAGE_URL = "https://qa-desk.stand.praktikum-services.ru"

TITLE_MODAL_WINDOW = 'Чтобы разместить объявление, авторизуйтесь'