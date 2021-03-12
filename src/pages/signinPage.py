from selenium import webdriver
from pages .basePage import BasePage
from locators.signin_locator import SigninLocators


class SignInPage(BasePage):

    #Constructor
    def __init__(self, driver):
        super().__init__(driver)

    #sign in action   
     
    def signInAction(self, username, password):
        self.el_send_keys(SigninLocators.USER_NAME_FIELD, username)
        self.el_send_keys(SigninLocators.PASSWORD_FIELD, password)
        self.el_click(SigninLocators.SIGNIN_BUTTON)

