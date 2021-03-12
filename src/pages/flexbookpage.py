from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from locators.flexbook_page_locators import FlexbookPageLocators
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeLocators
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeCustomizeLocators




class FlexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

         
    def selectOptions(self, language, subject, grade):
        # fbselect = BasePage(self.driver)
        lan =self.selectItem(FlexbookPageLocators.FB_LANGUAGE_DROPDOWN, language)
        sub = self.selectItem(FlexbookPageLocators.FB_SUBJECT_DROPDOWN, subject)
        grade = self.selectItem(FlexbookPageLocators.FB_GRADES_DROPDOWN, grade)
        
        self.el_click(FlexbookPageLocators.FB_SEARCH)
        #return(language, subject, grade)
        
        
    def title(self, title):
        return self.el_get_title(title)  
        
    #def checkWords(self, language, subject, grade, title):