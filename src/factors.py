#!/usr/local/bin/env python3
import unittest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from select import select
from selenium.webdriver.support.select import Select
class assertFactors(unittest.TestCase):
    #Asserting the title Prime and Composite Numbers to section name


    def setUp(self):
        #Logging In process
        
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.driver.get('http://www.ck12.org')
        self.driver.implicitly_wait(3)
        popup = None
        try:
            popup = self.driver.find_element_by_xpath("//div[@id='welcomePopup']")
        except:
            print("welcomePopup not available")

        if popup is not None:
            self.driver.find_element_by_xpath("//a[contains(text(),'×')]").click()   
        time.sleep(3)

        sign_in = self.driver.find_element_by_xpath("//span[contains(text(),'sign in')]")
        sign_in.click()
        self.driver.implicitly_wait(3)
        user_name = self.driver.find_element_by_name('login')
        user_name.send_keys('testmail.dailyjobs+teacher@gmail.com')
        password = self.driver.find_element_by_name('token')
        password.send_keys('Shopana@123')
        signIn = self.driver.find_element_by_xpath("//input[@class='btn button sign-in-submit pretty-button js-sign-in-submit tangerine standard']")
        signIn.click()
        time.sleep(7)
    def test_subject(self):
        driver = self.driver   
        # Click on subject im menu bar
        subjects = driver.find_element_by_xpath("//i[@class='icon-standards sc-kpOJdX ftFyjn']")
        subjects.click()
        #Select Arithmatic in Math by Subject
        arithmatic = driver.find_element_by_xpath("//body/div[@id='content-container']/div[@id='content-area']/div[@id='browse-grid-wrapper']/div[1]/div[1]/div[2]/div[1]/div[3]/ul[1]/li[1]/a[1]")
        arithmatic.click()
        #Click on Factors dropdown arrow
        factors = driver.find_element_by_xpath("//span[@title='Factors']")
        factors.click()
        # pc_num_value = factors.find_elements_by_tag_name('span')
        # pc_num_name = []

        # for name in pc_num_value:
        #     text1 = name.text1
        #     print('topic: '+text1)
        #     pc_num_name.append(text1)
        #select Prime and Composite Numbers
        pc_Num = driver.find_element_by_xpath("//span[contains(text(),'Prime and Composite Numbers')]")
        pc_Num.click()
        

        #Get the topic name
        topics = driver.find_element_by_xpath("//div[@class='js-components-newspaper-Header-Header__navigation_header___2c-XW']")
        topic_items = topics.find_elements_by_tag_name('span')
        topic_items_list = []

        for item in topic_items:
            text = item.text
            print(text)
            topic_items_list.append(text)
            #assert topic name
            self.assertIn("Prime and Composite Numbers", topic_items_list)
            

if __name__ == "__main__":
    unittest.main()



