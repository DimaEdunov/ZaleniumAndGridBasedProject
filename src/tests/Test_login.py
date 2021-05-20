import time

import allure
import pytest

from page_object.main_page_screen import main_page_screen
from page_object.login_page_screen import login_page_screen


@pytest.mark.usefixtures("driver")
class Test_login:

    @allure.feature('Login')
    @allure.story('wrong password test')
    @pytest.mark.regression
    @pytest.mark.run(order=1)
    def test_login_wrong_password(self, driver):

        print("Debug - 1")

        # Object #1 - Cyrebro Main Page
        main_page = main_page_screen(driver)
        main_page.go_to()

        print("Debug - 2")

        main_page.open_login_popup()
        print("Debug - 3")

        # Object #2 - Cyrebro Login Screen
        login_page = login_page_screen(driver)
        login_page.perform_login()
        print("Debug - 4")

        login_page.wrong_password_login_verification()
        print("Debug - 5")

        # time.sleep(3)
        # driver.quit()



