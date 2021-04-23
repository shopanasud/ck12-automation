#!/usr/bin/env python3
import pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from locators.flexbook_page_locators import FlexbookPageLocators
from locators.signin_locator import SigninLocators
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeLocators as ALGEBRA, FBMathAlgeb8GradeCustomizeLocators as ALGEBRACUS
from selenium.webdriver.support.ui import Select
from pages.basePage import BasePage
from pages.landingPage import LandingPage
from pages.signinPage import SignInPage
from pages.flexbookpage import FlexPage
from pages.fbBrowseList_page import FbBrowseListPage
from parameterized import parameterized, parameterized_class
from pages.customizePage import CustomizePage


class TestFlexBook1Assert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://www.ck12.org')
        time.sleep(2)

        # Signin button
        self.landingpage = LandingPage(self.driver)
        signin_modal = self.landingpage.signInWindow(self.driver)
        signin_modal.signInAction(
            "testmail.dailyjobs+teacher@gmail.com", "Shopana@123")
        time.sleep(4)

    def test_user_name(self):
        driver = self.driver
        # check for user name in home page
        find_user_name = driver.find_element_by_xpath(
            "//span[@class='sc-csuQGl hrnDev']")
        print(find_user_name.text)
        assert "SHOPANA" in find_user_name.text

    def test_flexbook_page(self):

        # Selecting flexbook from explore
        explore = BasePage(self.driver)
        explore.selectItem(FlexbookPageLocators.FB_EXPLORE_MENU,
                           FlexbookPageLocators.FB_FLEXBOOK_OPTION)
        title = explore.el_get_title("FlexBooks® | CK-12 Foundation")
        print(title)

    @parameterized.expand([
        ("English", "Algebra", "Middle School",
         "Algebra Flexbooks® for Middle School in English | CK-12 Foundation"),
        ("English", "Math", "Middle School",
         "Math Flexbooks® for Middle School in English | CK-12 Foundation"),
        ("English", "Arithmetic", "Middle School",
         "Arithmetic Flexbooks® for Middle School in English | CK-12 Foundation"),
        ("English", "Algebra", "High School",
         "Algebra Flexbooks® for High School in English | CK-12 Foundation")
    ])
    def test_flexbook_selectOptions(self, lang, sub, grade, title):
        # Selecting the dropdown - Language, Subject, Grade and check for the items are present in Title
        self.driver.get(
            "https://www.ck12.org/fbbrowse/?_ga=2.236491137.14732433.1612994297-1650535856.1612577864")
        fbselect = FlexPage(self.driver)
        words = fbselect.selectOptions(lang, sub, grade)
        newTitle = fbselect.el_get_title(title)
        print(newTitle)
        items = [lang, sub, grade]
        for i in items:
            self.assertIn(i, newTitle, msg="I am not true")

    def test_fb_select(self):
        # #choose 8th grade Algebra from the flexbooks
        self.driver.get(
            "https://www.ck12.org/fbbrowse/list/?Subject=Algebra&Language=English&Grade=Middle%20School")
        book = FbBrowseListPage(self.driver)
        assert book.checkMatch()

    def test_customizeBookTitle(self):
        # Change the tiltle of the flexbook
        self.driver.get(
            "https://www.ck12.org/book/CK-12-Middle-School-Math-Concepts-Grade-8/")
        custom = CustomizePage(self.driver)
        assert custom.checkTitle("Sho:Algebra")
        assert custom.checkCreator("SHOPANA")

    def test_customizeChapterTitle(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        custom = CustomizePage(self.driver)
        assert custom.customChapTitle("Sho:Real Number Properties")

    def test_chapDragDrop(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        dragDrop = CustomizePage(self.driver)
        assert dragDrop.checkDragDrop()

    def test_addNewChap(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        addNew = CustomizePage(self.driver)
        assert addNew.addChapter("New Chapter of Algebra")

    def test_deleteChap1(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        deleteChap = CustomizePage(self.driver)
        assert deleteChap.removeChapter()

    def test_toggleExpand(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        expand = CustomizePage(self.driver)
        expand.expandToggle()
        print("Expanded the section")

    def test_readDragDrop(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        dragdrop = CustomizePage(self.driver)
        assert dragdrop.checkReadDragDrop()

    def test_addNewRead(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        newRead = CustomizePage(self.driver)
        assert newRead.addRead("Real Numbers problems")

    def test_removeRead(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        newRead = CustomizePage(self.driver)
        assert newRead.removeRead()

    def test_renameRead(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        renameRead = CustomizePage(self.driver)
        assert renameRead.renameRead("Sho:Variable Expressions")

    def test_move_read_diff_chap(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        mv_read = CustomizePage(self.driver)
        assert mv_read.move_read_diff_chap()

    def test_moveTo_dropDown_1to5(self):
        self.driver.get(
            "https://www.ck12.org/editor/book/CK-12-Algebra-Basic/r32/")
        time.sleep(3)
        mv_read = CustomizePage(self.driver)
        assert mv_read.move_to_dropDown()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
