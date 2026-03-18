from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker

# Генераторы данных
def create_email():
    fake = Faker()
    return fake.email()

def create_password():
    fake = Faker()
    return fake.password(length=12)