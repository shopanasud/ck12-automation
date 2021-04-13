from selenium import webdriver
from pages.basePage import BasePage
from locators.staticFooterLocators import StaticFooterLocators as SFL
import time


class staticPageFooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    test2 = "hello2"

    def overViewModal(self):

        self.el_click(SFL.LINK_OVERVIEW)
        actual_heading = self.el_get_text(SFL.MODAL_OVERVIEW_HEADING)
        expected_heading = SFL.TEXT_OVERVIEW
        print(f'Actual heading of Overview: {actual_heading}')
        print(f'Expected heading of Overview: {expected_heading}')
        self.el_click(SFL.MODAL_OVERVIEW_CLOSE)
        return actual_heading == expected_heading

    def eMailModal(self):
        self.el_click(SFL.LINK_EMAIL)
        actual_heading = self.el_get_text(SFL.MODAL_EMAIL_HEADING)
        expected_heading = SFL.TEXT_EMAIL
        print(f'Actual heading of share Email: {actual_heading}')
        print(f'Expected heading of share Email: {expected_heading}')
        self.el_click(SFL.MODAL_EMAIL_CLOSE)
        return actual_heading == expected_heading
