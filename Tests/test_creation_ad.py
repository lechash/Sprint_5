import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data import *
from locators import *

class TestCreateAdUnauthorizedUser:
    def test_create_ad_unauthorized_user_shows_modal_with_correct_title(self, open_main_page):
        driver, wait = open_main_page

        # Нажимаем кнопку «Разместить объявление»
        create_ad_button = wait.until(EC.element_to_be_clickable(BUTTON_CREATE_AD))
        create_ad_button.click()

        # Ждём появления модального окна (оно уже содержит нужный текст)
        modal_window = wait.until(EC.visibility_of_element_located(NOTIFICATION_MODAL))

        # Проверяем, что модальное окно отображается и содержит правильный текст
        assert modal_window.is_displayed() and TITLE_MODAL_WINDOW in modal_window.text

class TestCreateAdAuthorizedUser:
    def test_create_advertisement_by_authorized_user(self, user_logged_in):
        # Авторизация
        driver, wait, login_successful = user_logged_in

        # Открываем форму создания объявления
        create_ad_button = wait.until(EC.element_to_be_clickable(BUTTON_CREATE_AD))
        create_ad_button.click()

        # Заполняем поля формы объявления
        
        # Поле «Название»
        title_field = wait.until(EC.element_to_be_clickable(INPUT_TITLE))
        title_field.clear()
        title_field.send_keys(advertisement.product_name)

        # Поле «Описание товара»
        desc_field = wait.until(EC.element_to_be_clickable(INPUT_DESCRIPTION))
        desc_field.clear()
        desc_field.send_keys(advertisement.description)

        # Поле «Стоимость»
        price_field = wait.until(EC.element_to_be_clickable(INPUT_PRICE))
        price_field.clear()
        price_field.send_keys(str(advertisement.price))

        # Выбираем категорию из Dropdown
        category_dropdown = wait.until(EC.element_to_be_clickable(DROPDOWN_CATEGORY))
        category_dropdown.click()
        category_option = wait.until(EC.element_to_be_clickable(SELECT_CATEGORY))
        category_option.click()

        # Выбираем город из Dropdown
        city_dropdown = wait.until(EC.element_to_be_clickable(DROPDOWN_CITY))
        city_dropdown.click()
        city_option = wait.until(EC.element_to_be_clickable(SELECT_CITY))
        city_option.click()

        # Выбираем состояние товара (RadioButton)
        driver.find_element(*RADIO_CONDITION).click()

        # Нажимаем кнопку «Опубликовать» и переходим на главную, затем в ЛК и ищем раздел «Мои объявления»
        wait.until(EC.element_to_be_clickable(BUTTON_PUBLISH)).click()
        wait.until(EC.invisibility_of_element_located(BUTTON_PUBLISH))
        
        driver.execute_script("window.scrollTo(0, 0);")
        wait.until(EC.element_to_be_clickable(USER_AVATAR)).click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located(SECTION_MY_ADS))

        # Ищем созданное объявление
        ads = wait.until(EC.presence_of_all_elements_located(ITEM_AD))
        found_ad = any(advertisement.product_name in ad.text for ad in ads)

        # Assert: проверяем, что объявление отображается в профиле
        assert found_ad, f"Объявление '{advertisement.product_name}' не найдено в профиле пользователя"

