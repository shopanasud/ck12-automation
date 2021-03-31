import pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basePage import BasePage
from pages.staticPageFooter import staticPageFooter
from locators.staticFooterLocators import StaticFooterLocators as SFL


class TestStaticPageFooter(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('http://www.ck12.org')
        time.sleep(3)

    # Check whether the links of the page are clickable and asserting the title of each page

    def test_checkTitle(self):
        title_of = BasePage(self.driver)
        test_dict = SFL.footer_links  # Parameters from the dictionary
        # Itrating the locators from the dictionary
        for i in test_dict:
            # converting the string to tuple
            locators = tuple(map(str, i.split(",")))
            title_of.el_click(locators)
            time.sleep(3)
            # Getting the Length of the window handles
            length = len(self.driver.window_handles)
            print(f'No. of Windows open: {length}')
            if length >= 2:
                parentWin = self.driver.window_handles[0]
                chldwin = self.driver.window_handles[1]
                self.driver.switch_to_window(chldwin)
                new_title = self.driver.title
                print(f'Expected: {test_dict[i]}')
                print(f'Actual: {new_title}')
                self.assertIn(test_dict[i], new_title,
                              "Page Titles don't Match")
                self.driver.close()
                self.driver.switch_to_window(parentWin)

            else:
                print("Only one window")
                new_title = self.driver.title
                print(f'Expected: {test_dict[i]}')
                print(f'Actual: {new_title}')
                self.assertIn(test_dict[i], new_title,
                              "Page Titles don't Match")
            self.driver.get("http://www.ck12.org")

    # Asserting the Heading of the page
    def test_modal_heading(self):
        header_of = staticPageFooter(self.driver)
        assert header_of.overViewModal()
        assert header_of.eMailModal()

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
