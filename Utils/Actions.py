import logging
import os
import sys

from appium.webdriver.common.appiumby import AppiumBy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils import constants
from robot.api.deco import not_keyword
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Actions:
    def __init__(self, driver):
        self.driver = driver
        self.AppiumBy = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH
        }

    @not_keyword
    def wait_element_to_be_visible(self, appium_by: str, locator: str, wait_timeout: int=5):
        try:
            element = WebDriverWait(self.driver, wait_timeout).until(EC.visibility_of(self.driver.find_element(self.AppiumBy[appium_by], locator)))
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")
        return element

    @not_keyword
    def check_element_displayed(self, appium_by: str, locator: str, wait_timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, wait_timeout).until(
                EC.visibility_of(self.driver.find_element(self.AppiumBy[appium_by], locator)))
            return True
        except Exception as e:
            logging.info(f"element is not visible and the error is: {e}")
            return False

    @not_keyword
    def click_element(self, appium_by: str, locator: str, wait_timeout: int = 5):
        try:
            element = WebDriverWait(self.driver, wait_timeout).until(EC.element_to_be_clickable(self.driver.find_element(self.AppiumBy[appium_by], locator)))
            element.click()
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")

    @not_keyword
    def enter_text(self, appium_by: str, locator: str, text: str, wait_timeout: int = 5):
        try:
            element = self.wait_element_to_be_visible(appium_by, locator, wait_timeout)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")

    @not_keyword
    def element_to_be_clickable(self, appium_by: str, locator: str, wait_timeout: int = 5):
        try:
            clickable_element = WebDriverWait(self.driver, wait_timeout).until(EC.element_to_be_clickable(self.driver.find_element(appium_by, locator)))
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")
        return clickable_element

    @not_keyword
    def element_to_be_invisible(self, appium_by: str, locator: str, wait_timeout: int = 5):
        try:
            clickable_element = WebDriverWait(self.driver, wait_timeout).until(EC.invisibility_of_element_located(self.driver.find_element(appium_by, locator)))
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")
        return clickable_element

    @not_keyword
    def get_element_text(self, appium_by: str, locator: str, wait_timeout: int = 5):
        try:
            element = self.wait_element_to_be_visible(appium_by, locator, wait_timeout)
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")
        return element.text

    @not_keyword
    def press_enter(self, appium_by: str, locator: str, wait_timeout: int = 5):
        try:
            element = self.wait_element_to_be_visible(appium_by, locator, wait_timeout)
            element.send_keys(Keys.ENTER)
        except Exception as e:
            raise ValueError(f"an error occurred: {str(e)}")


    @not_keyword
    def set_app_to_background(self, seconds: int):
        self.driver.background_app(seconds)

    @not_keyword
    def activate_app(self):
        activity_app = constants.get_appium_capability("appPackage")
        self.driver.activate_app(activity_app)
