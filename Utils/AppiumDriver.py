import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from appium import webdriver
from appium.options.common import AppiumOptions
from Utils import constants

class AppiumDriver:
    _driver = None

    @classmethod
    def setup_appium_driver(cls):
        logging.info(constants.get_appium_capabilities())
        desired_caps = AppiumOptions().load_capabilities(caps=constants.get_appium_capabilities())
        cls._driver = webdriver.Remote(constants.appium_server_url, options=desired_caps)
        cls._driver.implicitly_wait(10)
        logging.info(f"driver: {cls._driver}")


    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls.setup_appium_driver()
        return cls._driver
