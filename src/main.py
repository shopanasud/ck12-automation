#!/usr/bin/env python3

import unittest
from selenium import webdriver
import time
from pages.landingPage import LandingPage
from pages.signinPage import SignInPage

class LandingPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('http://www.ck12.org')
        time.sleep(4)

        self.landingpage = LandingPage(self, driver)
        self.landingpage.signInWindow

        sign_in = self.driver.find_element_by_xpath("//li[@id='top_nav_signin']")
        # sign_in.click()
        # time.sleep(4)
        # #sing in with valid teacher credentials into SingIn window
        # user = self.driver.find_element_by_xpath("//body/div[@id='sign-in-modal']/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]")
        # password = self.driver.find_element_by_xpath("//body/div[@id='sign-in-modal']/div[1]/div[3]/div[1]/div[1]/div[1]/input[2]")
        # user.send_keys("teacher777@gmail.com")
        # password.send_keys("test123")
        # print("credentials: user-", user, "password-", password)
        # signInButton = self.driver.find_element_by_xpath("//body/div[@id='sign-in-modal']/div[1]/div[3]/div[1]/div[1]/div[1]/input[4]")
        # signInButton.click()
        # time.sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()           
