import pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basePage import BasePage
from parameterized import parameterized, parameterized_class
from pages.staticPageFooter import staticPageFooter
from locators.staticFooterLocators import StaticFooterLocators as SFL


class TestStaticPageFooter(unittest.TestCase):
    #Test done using parameterization
    
    def setUp(self):
        
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('http://www.ck12.org')
        time.sleep(3)
    @parameterized.expand([
        (SFL.LINK_OUR_MISSION, "Mission | CK-12 Foundation"),
        (SFL.LINK_MEET_THE_TEAM, "Team | CK-12 Foundation"),
        (SFL.LINK_PARTNERS, "Partners | CK-12 Foundation"),
        (SFL.LINK_PRESS, "Press | CK-12 Foundation"),
        (SFL.LINK_CAREERS, "Passionate about education?So are we. | CK-12 Foundation"),
        (SFL.LINK_SECURITY, "Security at CK-12 Foundation | CK-12 Foundation"),
        (SFL.LINK_STATUS, "CK-12 Foundation Status"),
        (SFL.LINK_SUCCESS_STORIES, "Success Stories | CK-12 Foundation"),
        (SFL.LINK_BLOG, "CK-12 Blog | General information about CK-12"),
        (SFL.LINK_OVERVIEW, "Overview | CK-12 Foundation"),
        (SFL.LINK_CK12_USAGE_MAP, "CK-12 Usage Map | CK-12 Foundation"),
        (SFL.LINK_TESTIMONIALS, "CK-12 Testimonials | CK-12 Foundation"),
        (SFL.LINK_CERTIFIED_EDUCATOR_PROGRAM, "Certified Educator Program | CK-12 Foundation"),
        (SFL.LINK_WEBINARS, "Webinars | CK-12 Foundation"),
        (SFL.LINK_CK12_RESOURCES, "Overview | CK-12 Foundation"),
        (SFL.LINK_PILOT_PROGRAM, "Pilot Program | CK-12 Foundation"),
        (SFL.LINK_HELP, "Help Center"),
        (SFL.LINK_CONTACT_US, "Contact Us | CK-12 Foundation"),
        (SFL.LINK_TOOLS_AND_APPS, "Tools and Apps | CK-12 Foundation"),
        (SFL.LINK_COLLEGE_FLEXBOOKS, "K-12 FlexBooks® & Concepts | CK-12 Foundation"),
        (SFL.LINK_BRAINGENIE, "Braingenie"),
        (SFL.LINK_TERMS_OF_USE, "Terms of Use | CK-12 Foundation"),
        (SFL.LINK_PRIVACY, "Privacy Policy | CK-12 Foundation"),
        (SFL.LINK_ATTRIBUTION_GUIDE, "Attribution Guidelines")
        
    ])
    
    def test_check_title(self, locator, title):
        #Asserting the Title of the page of each footer links
        title_of = staticPageFooter(self.driver)
        result = title_of.title(locator, title)
        assert result  == True
        self.driver.get("http://www.ck12.org")
        
        
    
    
    def tearDown(self):
        
        self.driver.quit()

    
if __name__ == "__main__":
    unittest.main()       


