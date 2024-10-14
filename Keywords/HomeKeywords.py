import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pom.HomePage import HomePage
from Utils.Actions import Actions
from Utils.AppiumDriver import AppiumDriver

class HomeKeywords:
    def __init__(self):
        self.driver = AppiumDriver.get_driver()
        self.actions = Actions(self.driver)
        self.home_page = HomePage(self.driver)

    def set_delivery_address(self, address: str):
        self.home_page.allow_track_location()
        self.home_page.search_for_location(address)
        self.home_page.select_first_location()

    def verify_home_screen_displayed_successfully(self):
        screen_displayed = self.home_page.verify_home_screen_displayed()
        assert screen_displayed is True, "Home screen not displayed"