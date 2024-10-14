import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
from Utils.Actions import Actions
from Resources.locators import locators

class HomePage:
    def __init__(self, driver):
        self.actions = Actions(driver)
        self.home_locators = locators["home_locators"]

    def allow_track_location(self) -> None:
        logging.info("Navigate To Home")
        logging.info(self.home_locators["allowLocationWhileUseApp"][0], self.home_locators["allowLocationWhileUseApp"][1])
        self.actions.click_element(self.home_locators["allowLocationWhileUseApp"][0], self.home_locators["allowLocationWhileUseApp"][1])

    def search_for_location(self, address: str):
        self.actions.click_element(self.home_locators["selectLocation"][0], self.home_locators["selectLocation"][1])
        self.actions.click_element(self.home_locators["searchLocationField"][0], self.home_locators["searchLocationField"][1])
        self.actions.enter_text(self.home_locators["searchLocationInput"][0], self.home_locators["searchLocationInput"][1], text=address)

    def select_first_location(self):
        self.actions.click_element(self.home_locators["firstAddressOption"][0], self.home_locators["firstAddressOption"][1])
        self.actions.click_element(self.home_locators["confirmLocation"][0], self.home_locators["confirmLocation"][1])
        self.actions.click_element(self.home_locators["saveContinue"][0], self.home_locators["saveContinue"][1])

    def verify_home_screen_displayed(self) -> bool:
        return self.actions.check_element_displayed(self.home_locators["homeBottomIcon"][0], self.home_locators["homeBottomIcon"][1])

