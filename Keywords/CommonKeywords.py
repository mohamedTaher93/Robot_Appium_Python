import os
import sys

from robot.api.deco import keyword
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pom.HomePage import HomePage
from Utils.Actions import Actions
from Utils.AppiumDriver import AppiumDriver

class CommonKeywords:
    def __init__(self):
        self.driver = AppiumDriver.get_driver()
        self.actions = Actions(self.driver)
        self.home_page = HomePage(self.driver)

    @keyword("Launch HungerStation Application")
    def open_application(self):
        return self.driver

    @keyword("Close HungerStation Application")
    def close_application(self):
        self.driver.quit()

