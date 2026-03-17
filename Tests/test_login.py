import pytest
from test_data import MAIN_PAGE_URL
from locators import *
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_login_redirects_to_main_page(self, user_logged_in):
        driver, wait, login_successful = user_logged_in
        
        assert driver.current_url.startswith(MAIN_PAGE_URL)

    def test_login_displays_user_avatar(self, user_logged_in):
        driver, wait, login_successful = user_logged_in

        avatar = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        assert avatar.is_displayed()
    def test_login_displays_user_name_with_user_text(self, user_logged_in):
        driver, wait, login_successful = user_logged_in

        user_name_element = wait.until(EC.visibility_of_element_located(NAME_USER))
        user_name_text = user_name_element.text
        assert "User" in user_name_text