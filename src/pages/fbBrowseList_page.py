from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.landingPageLocators import LandingPageLocators
from pages.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from locators.flexbook_page_locators import FlexbookPageLocators
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeLocators as FL
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeCustomizeLocators




class FbBrowseListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
    def selectBook(self):
        self.bookTitle = self.el_get_text(FL.FB_MATH_ALGEBRA_8GRADE)
        self.el_click(FL.FB_MATH_ALGEBRA_8GRADE)
        print(f'From fbBrowse page: {self.bookTitle}')
        self.pageTitle = self.el_get_text(FL.FB_BOOK)
        print(f'From selectedBook page: {self.pageTitle}') 
        
    
    def checkMatch(self):
        self.selectBook()
        return self.bookTitle == self.pageTitle
        # if self.bookTitle == self.pageTitle:
        #     print(True)
        # else:
        #     print(False)    
        
        
           