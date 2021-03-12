import pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




class TestLoggingIn(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('chromedriver')
        cls.driver.get('https://dev.teamroadz.com/auth/login')
        time.sleep(3)
    
    
    def test_login1(self):
        
        self.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@name='email']").send_keys("shopana@roadz.com")
        self.driver.find_element_by_xpath("//input[@placeholder='your password']").send_keys("Welcome2Roadz!")
        self.driver.find_element_by_xpath("//span[contains(.,'Log In')]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//p[normalize-space()='Solutions']").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.find_element_by_xpath("//i[@class='nc-icon nc-simple-add']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        
        radio = self.driver.find_element_by_xpath("div[class='form-check-radio mr-4 mt-2'] span:nth-child(3)")
        radio.location_once_scrolled_into_view
        radio.click()
        time.sleep(4)
        print(radio.is_selected())
        
        
        
        
        
        
    
    @classmethod
    def tearDownClass(cls): 
        cls.driver.quit()

    
if __name__ == "__main__":
    unittest.main()       


