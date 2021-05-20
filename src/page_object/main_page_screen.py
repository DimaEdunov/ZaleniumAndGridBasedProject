import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class main_page_screen():

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get("https://www.cyrebro.io/")

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="go to main page",
                      attachment_type=AttachmentType.PNG)

    def open_login_popup(self):
        login_button_xpath = "(//ul//li[contains(@id,'sec-nav-menu-item')]//a)[1]"

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

        first_screen_identifier = self.driver.window_handles[0]
        second_screen_identifier = self.driver.window_handles[1]

        self.driver.switch_to.window(second_screen_identifier)

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="open login popup",
                      attachment_type=AttachmentType.PNG)


