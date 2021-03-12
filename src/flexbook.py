import unittest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from select import select
from selenium.webdriver.support.select import Select
class FlexBook(unittest.TestCase):
    #Tiny MCE editor renders properly in Flexbook 2.0
    def setUp(self):
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get('http://www.ck12.org')
        popup = driver.find_element_by_xpath("//div[@id='welcomePopup']")
        driver.implicitly_wait(3)
        sign_in = driver.find_element_by_id('top_nav_signin')
        sign_in.click()
        driver.implicitly_wait(3)
        user_name = driver.find_element_by_name('login')
        user_name.send_keys('testmail.dailyjobs+teacher@gmail.com')
        password = driver.find_element_by_name('token')
        password.send_keys('Shopana@123')
        signIn = driver.find_element_by_xpath("//input[@class='btn button sign-in-submit pretty-button js-sign-in-submit tangerine standard']")
        signIn.click()
        time.sleep(7)

        
        explore = driver.find_element_by_xpath("//header/nav[1]/section[1]/ul[1]/li[5]/a[1]")
        explore.click()
        flexbook_2 = driver.find_element_by_xpath("//div[contains(text(),'in a new, interactive platform')]")
        flexbook_2.click()
        get_started = driver.find_element_by_xpath("//b[contains(text(),'Get Started')]")
        get_started.click()
        time.sleep(1)
        select_book = driver.find_element_by_xpath("//b[contains(text(),'CK-12 Interactive Geometry')]")
        select_book.click()
        time.sleep(3)
        choose = driver.find_element_by_xpath("//div[contains(text(),'Choose')]")
        choose.click()
        customize = driver.find_element_by_xpath("//span[contains(text(),'Customize')]")
        customize.click()
        time.sleep(5)
        expand_toggle = driver.find_element_by_xpath("//body/div[@id='content-container']/div[@id='contentwrap']/div[@id='content']/article[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]")
        expand_toggle.click()
        click_ellipsis = driver.find_element_by_xpath("//body[1]/div[4]/div[5]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[3]/a[1]/span[1]")
        click_ellipsis.click()
        edit = driver.find_element_by_xpath("//body[1]/div[4]/div[5]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[3]/a[1]")
        edit.click()
        time.sleep(3)
        popup_1 = driver.find_element_by_xpath("//body/div[@id='save_dialog']/div[2]/div[1]")
        if popup_1 is not None:
            driver.find_element_by_xpath("//body/div[@id='save_dialog']/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
            driver.find_element_by_xpath("//div[contains(text(),'Got it!')]").click()
        title = driver.find_element_by_xpath("//input[@id='txt_artifacttitle']")
        title.click()
        title_clear = driver.find_element_by_xpath("//input[@id='txt_artifacttitle']")
        title_clear.clear()
        time.sleep(1)
        title_edit = driver.find_element_by_xpath("//input[@id='txt_artifacttitle']")
        title_edit.send_keys('Sho:Three Dimensions')
        time.sleep(1)
        save_title = driver.find_element_by_id('new-modality-save')
        save_title.click()
        time.sleep(3)
        #driver.assertTrue(driver.is_element_present(By.CLASS_NAME,'mce-ico mce-i-bold'))
        # Check if Tiny MCE editor is found
        x = len(driver.find_elements_by_xpath("//div[@id='mceu_31-body']"))
        print(x)
        
        # if x > 0:
        #     print('Tiny MCE Editor found')
        # else:
        #     print('Test Failed')   
        assert x > 0

    #Tiny MCE editor renders properly in Flexbook 
    # def test_tiny_MCE_Editor_flexbook(self):
    #     driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    #     driver.get('http://www.ck12.org')
    #     popup = driver.find_element_by_xpath("//div[@id='welcomePopup']")
    #     driver.implicitly_wait(3)
    #     if popup is not None:
    #         driver.find_element_by_xpath("//a[contains(text(),'×')]").click()

    #     driver.implicitly_wait(10)
    #     sign_in = driver.find_element_by_id('top_nav_signin')
    #     sign_in.click()
    #     driver.implicitly_wait(3)
    #     user_name = driver.find_element_by_name('login')
    #     user_name.send_keys('testmail.dailyjobs+teacher@gmail.com')
    #     password = driver.find_element_by_name('token')
    #     password.send_keys('Shopana@123')
    #     signIn = driver.find_element_by_xpath("//input[@class='btn button sign-in-submit pretty-button js-sign-in-submit tangerine standard']")
    #     signIn.click()
    #     time.sleep(7)
    #     explore = driver.find_element_by_xpath("//header/nav[1]/section[1]/ul[1]/li[5]/a[1]")
    #     explore.click()
    #     flex_book = driver.find_element_by_xpath("//header/section[2]/ul[1]/li[2]/a[1]/div[1]/div[1]")
    #     flex_book.click()
    #     language = driver.find_element_by_xpath("//body/div[@id='fbbrowse-root']/div[1]/div[2]/div[1]/div[2]/div[3]/select[1]")
    #     select_lang = Select(language)
    #     select_lang.select_by_visible_text('English')
    #     time.sleep(1)
    #     subjects = driver.find_element_by_name('Subject')
    #     select_subj = Select(subjects)
    #     select_subj.select_by_value('Algebra')
    #     time.sleep(1)
    #     grades = driver.find_element_by_name('Grade')
    #     select_grd = Select(grades)
    #     select_grd.select_by_visible_text('All Grades')
    #     time.sleep(1)
    #     search = driver.find_element_by_xpath("//div[contains(text(),'Search FlexBooks®')]")
    #     search.click()
    #     book = driver.find_element_by_xpath("//a[contains(text(),'CK-12 Algebra - Basic')]")
    #     book.click()
    #     chapter = driver.find_element_by_xpath("//span[contains(text(),'Expressions, Equations, and Functions')]")
    #     chapter.click()
    #     section = driver.find_element_by_xpath("//span[contains(text(),'Variable Expressions')]")
    #     section.click()








if __name__ == "__main__":
    unittest.main()