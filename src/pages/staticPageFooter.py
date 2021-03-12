from selenium import webdriver
from pages.basePage import BasePage
from parameterized import parameterized, parameterized_class
from locators.staticFooterLocators import StaticFooterLocators as SFL
import time
from selenium.common.exceptions import NoSuchElementException   
from selenium.common.exceptions import TimeoutException


class staticPageFooter(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
         
        
    def modalPopUp(self, locator):
        #Check if Modal popup is available
        
        try:
            self.driver.find_element_by_xpath(SFL.MODAL_OVERVIEW[1])
        except NoSuchElementException: 
            return False
        
        # check if the modal popup is visible
        if self.driver.find_element_by_xpath(SFL.MODAL_OVERVIEW[1]).is_displayed():
            print("Element is displayed")
            
        else:
            print("Element is not displayed")   
            return False
        
        
       
        
        return True
    
    def getHeading(self):
        heading = self.el_get_text(SFL.MODAL_HEADING)
        print(f'Heading: {heading}')
        return heading
    
    def closeModal(self):
        return self.el_click(SFL.MODAL_CLOSE)
    
    
        
        
        