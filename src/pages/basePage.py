from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException
from customFunctions.selectFunction import Select1


# This parent class for all page classes.
# This class will have generic methods
class BasePage(object):

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # General methods

    def el_get(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))

    def el_get_all(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

    def el_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(by_locator)).click()
        time.sleep(1)

    def el_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)
        print("The text entered: ", text)

    def el_get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return element.text

    def el_is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return bool(element)

    def el_get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title

    def el_select(self, by_locator, value):
        select = Select1(self.el_get(by_locator))
        select.select_by_visible_partial_text(value)
        option = select.first_selected_option
        print(f'Select: {option.text}')

    def el_choose(self, by_locator, by_locators):

        self.el_click(by_locator)
        option = self.el_click(by_locators)

    def selectItem(self, DropDown, listItem):

        element = self.el_get(DropDown)
        if element.tag_name.lower() == "select":
            self.el_select(DropDown, listItem)
        else:
            self.el_choose(DropDown, listItem)

    def el_DragDrop(self, source, target):
        drag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(target))
        action = ActionChains(self.driver)
        action.click_and_hold(drag).move_to_element(
            drop).release(drop).perform()
        # action.drag_and_drop(drag, drop).perform()
        time.sleep(5)

    def switch_frame(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(*by_locator))
        self.driver.switch_frame(element)

    def window_scroll_down(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def el_present(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def el_visible(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def el_displayed(self, locator):
        ele = self.driver.find_element_by_xpath(locator)
        return ele.is_displayed()

    def el_selected(self, by_locator, is_selected):
        return WebDriverWait(self.driver, 10).until(
            EC.element_located_to_be_selected(by_locator, is_selected))

    def el_isTitle(self, title):
        return WebDriverWait(self.driver, 10).until(EC.title_is(title))

    def el_present_all(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))

    def move_and_get(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def switch_window_get_title(self):
        parent_win = self.driver.window_handles[0]
        child_win = self.driver.window_handles[1]
        self.driver.switch_to_window(child_win)
        time.sleep(3)
        new_title = self.driver.title
        time.sleep(1)
        self.driver.close()
        self.driver.switch_to_window(parent_win)
        return new_title

    def get_link_statusCode(self, tag_name, attribute):
        links = self.driver.find_elements_by_tag_name(tag_name)
        link_status = {}
        for link in links:
            source = link.get_attribute(attribute)
            if source != None:
                if source.startswith('http'):
                    head = requests.get(source)
                    status = head.status_code
                    link_status[source] = status
            else:
                print(f'none links: {link}')
        count = len(link_status)
        print(f'Total {tag_name} tag links: {count}')
        return link_status

    def el_get_attribute_val(self, by_locator, attribute):
        element = self.el_present(by_locator)
        return element.get_attribute(attribute)
