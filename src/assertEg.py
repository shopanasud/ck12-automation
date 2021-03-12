#!/usr/local/bin/env python3
import selenium
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from lib2to3.pgen2 import driver
class assertionsTypes(unittest.TestCase):
    @unittest.SkipTest
    def testAssertEqual(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('http://www.ck12.org')
        expectedTitle = "Free Online Textbooks, Flashcards, Adaptive Practice, Real World Examples, Simulations"
        actualTitle = driver.title
​        #assertEqual/NotEqual
        assertEqual(expectedTitle, actualTitle, "Not expected title")
        #self.assertNotEqual("TestTitle", actualTitle, "expecting different title")
        # assert True/False - provides the ability to the user for writing relational operators,
        # we can use language-specific relational operators to compare values inside the assertTrue method.
        # When we use relational operators, they will result in either True or False.
        assertTrue((actualTitle!="Google") & (actualTitle!="Selenium"), "title doesn't match")
    @unittest.SkipTest
    def testAssertIsNone(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('http://www.ck12.org')
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'sign in')]").click()
        time.sleep(4)
        #self.assertIsNone(driver.find_element_by_xpath("//div[@id='sign-in-modal']"))
        assertIsNotNone(driver.find_element_by_xpath("//div[@id='sign-in-modal']"))
​
    @unittest.SkipTest
    def testAssertIn(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('http://www.ck12.org')
        time.sleep(2)
        menu = driver.find_element_by_xpath("//ul[contains(@class, 'sc-hzDkRC jGsNo')]")
        menuItems = menu.find_elements_by_tag_name("li")
        menuItemsCaptions = []
        for item in menuItems:
            text = item.text
            print(text)
            menuItemsCaptions.append(text)
        # assertIn/assertNotIn
        assertIn("JOIN", menuItemsCaptions)
​
    @unittest.SkipTest
    def testAssertGreaterLess(self):
        assertGreater(100, 10)
        #self.assertGreaterEqual(100, 100)
        #self.assertLess(10, 100)
        #self.assertLessEqual(100, 100)
​
​
if __name__ == "__main__":
    unittest.main()