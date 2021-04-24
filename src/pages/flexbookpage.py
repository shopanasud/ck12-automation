from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from locators.flexbook_page_locators import FlexbookPageLocators
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeLocators
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeCustomizeLocators


class FlexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectOptions(self, language, subject, grade):
        # fbselect = BasePage(self.driver)
        lan = self.selectItem(
            FlexbookPageLocators.FB_LANGUAGE_DROPDOWN, language)
        sub = self.selectItem(
            FlexbookPageLocators.FB_SUBJECT_DROPDOWN, subject)
        grade = self.selectItem(FlexbookPageLocators.FB_GRADES_DROPDOWN, grade)

        self.el_click(FlexbookPageLocators.FB_SEARCH)
        # return(language, subject, grade)

    def title(self, title):
        return self.el_get_title(title)

    def check_text(self):
        text_available = {}
        texts = FlexbookPageLocators.TEXT
        for key in texts:
            txt = self.el_get(texts[key])
            text_available[key] = txt.text
        print(f'Available Text in the page: {text_available}')
        return text_available

    def check_textInOptions(self):
        option_txt = {}
        available_options = FlexbookPageLocators.TEXT_OPTIONS
        for key in available_options:
            lists = []
            options = self.el_get_all(available_options[key])
            for each in options:
                lists.append(each.text)
            option_txt[key] = lists
        print(f'List of Options: {option_txt}')
        return option_txt

    def check_image(self):
        result = {}
        img_source = {}
        images = FlexbookPageLocators.IMAGE
        for each in images:
            img = self.el_present(images[each])
            action = ActionChains(self.driver)
            action.move_to_element(img).perform()
            time.sleep(2)
            img_source[each] = img.get_attribute('src')
            result[each] = img.is_displayed()
        print(f'Presence of Image: {result}')
        print(f'Image source: {img_source}')
        count = len(img_source)
        print(f'Images Displayed: {count}')
        return img_source
