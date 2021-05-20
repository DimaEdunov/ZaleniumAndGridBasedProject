import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login_page_screen():

    def __init__(self, driver):
        self.driver = driver

    def perform_login(self):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.ID, "username"))).send_keys("aaaaaaaaa")

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.ID, "password"))).send_keys("Aa111111")

        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sign In')]"))).click()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name='post login session',
                      attachment_type=AttachmentType.PNG)

    def wrong_password_login_verification(self):

        time.sleep(3)
        print(len(self.driver.find_elements(By.XPATH, "//div[contains(text(),'Sign In')]")))

        if len(self.driver.find_elements(By.XPATH, "//div[contains(text(),'Sign In')]")) > 0:
            print("Wrong Password Inserted - Test Passed !")
            assert True

        else:
            print("Wrong Password Inserted - Login Was Successful - Tested Failed !")
            assert False


        allure.attach(self.driver.get_screenshot_as_png(),
                      name="false verification",
                      attachment_type=AttachmentType.PNG)
