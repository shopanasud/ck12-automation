from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.landingPageLocators import LandingPageLocators
from locators.signin_locator import SigninLocators
from pages.signinPage import SignInPage
from pages.basePage import BasePage


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def signInWindow(self, driver):
        self.el_click(LandingPageLocators.LANDING_SIGNIN_BUTTON)
        return SignInPage(self.driver)
