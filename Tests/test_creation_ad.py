import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from test_data import advertisement
from locators import *

class TestCreateAdUnauthorizedUser:
    def test_create_ad_unauthorized_user_shows_modal_with_correct_title(self, modal_window_appeared):
        #Тест: при попытке создать объявление неавторизованным пользователем модальное окно содержит правильный заголовок.     
        modal_window = modal_window_appeared

        # Проверяем заголовок модального окна
        modal_title = modal_window.find_element(*NOTIFICATION_MODAL)
        assert "Чтобы разместить объявление, авторизуйтесь" in modal_title.text

class TestCreateAdAuthorizedUser:
    def test_create_advertisement_by_authorized_user(self, user_logged_in, ad_creation_form_opened):
        # Шаг 1: Проверка авторизации (в начале теста)
        driver, wait, login_successful = user_logged_in

        if not login_successful:
            pytest.fail("Авторизация не удалась — тест не может быть выполнен")

        # Шаг 2: Открываем форму создания объявления
        driver, wait, form_opened = ad_creation_form_opened

        if not form_opened:
            pytest.fail("Не удалось открыть форму создания объявления — тест не может быть выполнен")

        # Шаг 3: заполняем поля формы объявления
        
        # Поле «Название»
        title_field = wait.until(EC.element_to_be_clickable(INPUT_TITLE))
        title_field.clear()
        title_field.send_keys("Тестовый товар для продажи")
        product_name = "Тестовый товар для продажи"

        # Поле «Описание товара»
        desc_field = wait.until(EC.element_to_be_clickable(INPUT_DESCRIPTION))
        desc_field.clear()
        desc_field.send_keys(advertisement.description)

        # Поле «Стоимость»
        price_field = wait.until(EC.element_to_be_clickable(INPUT_PRICE))
        price_field.clear()
        price_field.send_keys(str(advertisement.price))

        # Шаг 4: выбираем категорию из Dropdown
        category_dropdown = wait.until(EC.element_to_be_clickable(DROPDOWN_CATEGORY))
        category_dropdown.click()
        category_option = wait.until(EC.element_to_be_clickable(SELECT_CATEGORY))
        category_option.click()

        # Шаг 5: выбираем город из Dropdown
        city_dropdown = wait.until(EC.element_to_be_clickable(DROPDOWN_CITY))
        city_dropdown.click()
        city_option = wait.until(EC.element_to_be_clickable(SELECT_CITY))
        city_option.click()

        # Шаг 6: выбираем состояние товара (RadioButton)
        driver.find_element(*RADIO_CONDITION).click()

        # Шаг 7: нажимаем кнопку «Опубликовать» и переходим на главную, затем в ЛК и ищем раздел «Мои объявления»
        wait.until(EC.element_to_be_clickable(BUTTON_PUBLISH)).click()
        wait.until(EC.invisibility_of_element_located(BUTTON_PUBLISH))
        
        driver.execute_script("window.scrollTo(0, 0);")
        wait.until(EC.element_to_be_clickable(USER_AVATAR)).click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located(SECTION_MY_ADS))

        # Ищем созданное объявление
        ads = wait.until(EC.presence_of_all_elements_located(ITEM_AD))
        found_ad = any(product_name in ad.text for ad in ads)

        # Assert: проверяем, что объявление отображается в профиле
        assert found_ad, f"Объявление '{product_name}' не найдено в профиле пользователя"

class TestCreateAdNewUser:
    def test_create_advertisement_by_new_user(self, registered_user_with_ad_form):
        #        Тест: создание объявления новым пользователем.
        # Шаг 1–2: регистрация пользователя и открытие формы объявления (выполняется в фикстуре)
        driver, wait, email, password, form_opened = registered_user_with_ad_form

        if not form_opened:
            pytest.fail("Не удалось открыть форму создания объявления — тест не может быть выполнен")

        # Шаг 3: заполняем поля формы объявления
        
        # Поле «Название»
        title_field = wait.until(EC.element_to_be_clickable(INPUT_TITLE))
        title_field.clear()
        title_field.send_keys("Тестовый товар для продажи")
        product_name = "Тестовый товар для продажи"

        # Поле «Описание товара»
        desc_field = wait.until(EC.element_to_be_clickable(INPUT_DESCRIPTION))
        desc_field.clear()
        desc_field.send_keys(advertisement.description)

        # Поле «Стоимость»
        price_field = wait.until(EC.element_to_be_clickable(INPUT_PRICE))
        price_field.clear()
        price_field.send_keys(str(advertisement.price))

        # Шаг 4: выбираем категорию из Dropdown
        category_dropdown = wait.until(EC.element_to_be_clickable(DROPDOWN_CATEGORY))
        category_dropdown.click()
        category_option = wait.until(EC.element_to_be_clickable(SELECT_CATEGORY))
        category_option.click()

        # Шаг 5: выбираем город из Dropdown
        city_dropdown = wait.until(EC.element_to_be_clickable(DROPDOWN_CITY))
        city_dropdown.click()
        city_option = wait.until(EC.element_to_be_clickable(SELECT_CITY))
        city_option.click()

        # Шаг 6: выбираем состояние товара (RadioButton)
        driver.find_element(*RADIO_CONDITION).click()

        # Шаг 7: нажимаем кнопку «Опубликовать» и переходим на главную, затем в ЛК и ищем раздел «Мои объявления»
        wait.until(EC.element_to_be_clickable(BUTTON_PUBLISH)).click()
        wait.until(EC.invisibility_of_element_located(BUTTON_PUBLISH))
        
        driver.execute_script("window.scrollTo(0, 0);")
        wait.until(EC.element_to_be_clickable(USER_AVATAR)).click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(EC.visibility_of_element_located(SECTION_MY_ADS))

        # Ищем созданное объявление
        ads = wait.until(EC.presence_of_all_elements_located(ITEM_AD))
        found_ad = any(product_name in ad.text for ad in ads)

        # Assert: проверяем, что объявление отображается в профиле
        assert found_ad, f"Объявление '{product_name}' не найдено в профиле пользователя"

        