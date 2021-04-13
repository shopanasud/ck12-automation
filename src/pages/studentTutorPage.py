from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.basePage import BasePage
from locators.studentTutorLocators import StudentTutorLocators as STL
import time


class StudentTutorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # To close the curriculam bannner on the page
    def close_banner(self):
        self.el_click(STL.BANNER)

    # get Modal Subjects names
    def get_ModalSubjects(self):
        self.el_click(STL.LINK_CHOOSE_YOUR)
        subjects = []
        sub_modal = self.el_get_all(STL.MODAL_SUBJECTS)
        for i in sub_modal:
            subjects.append(i.text)
        print(f'Actual list in Modal: {subjects}')
        return subjects

    # get subjects in the footer
    def get_Subjects(self):
        subjects = []
        sub = self.el_get_all(STL.SUBJECT_TABS)
        for i in sub:
            subjects.append(i.text)
        print(f'Actual List: {subjects}')
        return subjects

    # get the Titlt of the subject topics of science in Choose your Subject link.
    def get_ModalTopicTitle(self):
        sub_list = self.get_ModalSubjects()
        print(sub_list)
        sub_locators = STL.MODAL_SUB_LOCATORS
        sub_topic_locators = STL.MODAL_SUB_TOPIC_LOCATORS
        lists = []
        for sub, sub_locator, topic_locator in zip(sub_list, sub_locators, sub_topic_locators):
            self.el_click(sub_locator)
            print(f'{sub} Tab Clicked')
            title = []
            topics = self.el_get_all(topic_locator)
            for topic in topics:
                topic.click()
                new_title = self.switch_window_get_title()
                title.append(new_title)
            lists.append(title)
        print(f'list of list: {lists}')
        return lists

    # get the Title of subject topics at the footer
    def get_TopicTitle(self):
        sub_list = self.get_Subjects()
        sub_locators = STL.SUBJECTS_LOCATORS
        sub_topic_locators = STL.SUB_TOPIC_LOCATORS
        lists = []
        for sub, sub_locator, topic_locator in zip(sub_list, sub_locators, sub_topic_locators):
            self.el_click(sub_locator)
            print(f'{sub} Subject Clicked')
            title = []
            topics = self.el_get_all(topic_locator)
            for topic in topics:
                topic.click()
                new_title = self.switch_window_get_title()
                title.append(new_title)
            lists.append(title)
        print(f'list of list: {lists}')
        return lists

    # To check the BrowseAll in Modal
    def check_ModalBrowseAll(self):
        self.el_click(STL.LINK_CHOOSE_YOUR)
        self.el_click(STL.LINK_BROWSE_ALL_FLEXBOOKS_MODAL_WINDOW_TEXT)
        title = self.switch_window_get_title()
        return title

    # Get all the Headings in DOM
    def get_HeadingTitle(self):
        headings = []
        all_heads = STL.TEXT_HEADERS
        for header in all_heads:
            head = self.el_present(header)
            action = ActionChains(self.driver)
            action.move_to_element(head).perform()
            time.sleep(1)
            headings.append(head.text)
        print(f'Headings of all the headers: {headings}')
        return headings

    # Get the text in testinonial
    def get_Testimonials_text(self):
        testimonials_txts = []
        elm = self.el_get(STL.CAROUSEL_CONTAINER)
        action = ActionChains(self.driver)
        action.move_to_element(elm).perform()
        element = STL.LINK_TESTIMONIALS
        testimonial_txt_locators = STL.TEXT_TESTIMONIALS
        for link, txt_loc in zip(element, testimonial_txt_locators):
            self.el_click(link)
            text_locators = self.el_present_all(txt_loc)
            for txt in text_locators:
                testimonials_txts.append(txt.text)
                time.sleep(2)
        print(f'Text in testimonial: {testimonials_txts}')
        return testimonials_txts

    # Get the text present in the page
    def get_AllText(self):
        actual_txt = []
        for content in STL.TEXT_LOCATORS:
            if len(content) > 1:
                page_txt = self.el_present_all(content)
                for txt in page_txt:
                    action = ActionChains(self.driver)
                    action.move_to_element(txt).perform()
                    time.sleep(1)
                    actual_txt.append(txt.text)
            else:
                single_content = self.el_present(content)
                action = ActionChains(self.driver)
                action.move_to_element(single_content).perform()
                time.sleep(1)
                actual_txt.append(content.text)
        print(f'Text under Paragraph tag name: {actual_txt}')
        return actual_txt

    # Get the text present in the modal
    def get_ModalText(self):
        self.el_click(STL.LINK_CHOOSE_YOUR)
        modal_txt_locators = STL.TEXT_IN_MODAL
        modal_text = []
        for each in modal_txt_locators:
            content = self.el_get(each)
            modal_text.append(content.text)
        print(f'Actual text in Modal window: {modal_text}')
        self.el_click(STL.LINK_CLOSE_BUTTON)
        return modal_text

    # Get the title of the pages
    def get_PageTitles(self):
        page_title = []
        links = STL.LINK_PAGE_TITLES
        for link in links:
            ele = self.el_present(link)
            action = ActionChains(self.driver)
            action.move_to_element(ele).perform()
            self.el_click(link)
            if len(self.driver.window_handles) > 1:
                title = self.switch_window_get_title()
                page_title.append(title)
            else:
                page_title.append(self.driver.title)
        print(f'PAge Titles: {page_title}')
        return page_title

    # Check the image presence and get the image source
    def check_ImagePresence(self):
        result = {}
        img_source = {}
        images = STL.IMAGE_LINKS
        for key in images:
            img = self.el_present(images[key])
            action = ActionChains(self.driver)
            action.move_to_element(img).perform()
            time.sleep(2)
            img_source[key] = img.get_attribute('src')
            result[key] = img.is_displayed()
        print(f'Presence of Image: {result}')
        print(f'Image source: {img_source}')
        count = len(img_source)
        print(f'Images Displayed: {count}')
        return img_source

    # Check the image presence and get the image source of the subject topic in the footer
    def check_imagePresence_sub(self):
        result = {}
        img_source = {}
        images = STL.SUB_IMAGE_LINKS
        subject = STL.SUBJECTS_LOCATORS
        sub_topic_locators = STL.SUB_TOPIC_LOCATORS
        for sub, top, key in zip(subject, sub_topic_locators, images):
            self.el_click(sub)
            topics = self.el_get_all(top)
            sub_img = self.el_present_all(images[key])
            for topic, img in zip(topics, sub_img):
                action = ActionChains(self.driver)
                action.move_to_element(topic).perform()
                time.sleep(2)
                img_source[topic.text] = img.get_attribute('src')
                result[topic.text] = img.is_displayed()
        print(f'Presence of Image: {result}')
        print(f'Image source: {img_source}')
        count = len(img_source)
        print(f'Images Displayed: {count}')
        return img_source

     # Check the image presence and get the image source of the subject topic in the modal
    def check_imagePresence_sub_modal(self):
        self.el_click(STL.LINK_CHOOSE_YOUR)
        result = {}
        img_source = {}
        images = STL.MODAL_SUB_IMAGE_LINKS
        subject = STL.MODAL_SUB_LOCATORS
        sub_topic_locators = STL.MODAL_SUB_TOPIC_LOCATORS
        for sub, top, key in zip(subject, sub_topic_locators, images):
            self.el_click(sub)
            topics = self.el_get_all(top)
            sub_img = self.el_present_all(images[key])
            for topic, img in zip(topics, sub_img):
                action = ActionChains(self.driver)
                action.move_to_element(img).perform()
                time.sleep(2)
                img_source[topic.text] = img.get_attribute('src')
                result[topic.text] = img.is_displayed()
        print(f'Presence of Image: {result}')
        print(f'Image Source: {img_source}')
        count = len(img_source)
        print(f'Images Displayed: {count}')
        return img_source

     # Check the image presence and get the image source of the testimonial
    def check_testimonialImage(self):
        elm = self.el_get(STL.CAROUSEL_CONTAINER)
        action = ActionChains(self.driver)
        action.move_to_element(elm).perform()
        result = {}
        img_source = {}
        images = STL.TESTIMONIAL_IMAGE
        carousals = STL.LINK_TESTIMONIALS
        for carousal, key in zip(carousals, images):
            self.el_click(carousal)
            img = self.el_present(images[key])
            time.sleep(4)
            img_source[key] = img.get_attribute('src')
            result[key] = img.is_displayed()
        print(f'Presence of Image: {result}')
        count = len(result)
        print(f'Images Displayed: {count}')
        print(f'Images source: {img_source}')
        return img_source

    # Check if the image is broken
    def get_brokenLinks(self):
        broken_link = {}
        tags = STL.LINK_IMAGE_TAGS
        for each in tags:
            status = self.get_link_statusCode(each, tags[each])
            for each in status:
                if (status[each] < 999 and status[each] >= 400):
                    broken_link[each] = status[each]
                else:
                    continue
        print(f'Broken links and the status: {broken_link}')
        count = len(broken_link)
        print(f'Number of Items broken: {count}')
        return broken_link

    # Locators of the links present in the modal to check the link source
    def get_linkSource_modal(self):
        self.el_click(STL.LINK_CHOOSE_YOUR)
        topic = {}
        img_sources = {}
        browse = self.el_get(
            STL.LINK_BROWSE_ALL_FLEXBOOKS_MODAL_WINDOW_TEXT)
        browseAll = browse.text
        src = browse.get_attribute('href')
        topic[browseAll] = src
        sub_locators = STL.MODAL_SUB_LOCATORS
        sub_topic_locators = STL.MODAL_SUB_TOPIC_LOCATORS
        topic_links_locator = STL.LINK_MODAL_SUBS
        for sub, top, link in zip(sub_locators, sub_topic_locators, topic_links_locator):
            self.el_click(sub)
            topics = self.el_get_all(top)
            links = self.el_get_all(link)
            for tpc, lnk in zip(topics, links):
                topic[tpc.text] = lnk.get_attribute('href')
        print(f'link sources: {topic}')
        return topic

    # Locators of the links present in the page to check the link source
    def get_linkSource(self):
        topic = {}
        for ele in STL.LINK_FOOTER_REST:
            item = self.el_get(ele)
            ActionChains(self.driver).move_to_element(item).perform()
            txt = item.text
            src = item.get_attribute('href')
            topic[txt] = src
        ActionChains(self.driver).move_to_element(
            self.el_get(STL.LINK_SUB_CONTAINER_FOOTER)).perform()
        sub_locators = STL.SUBJECTS_LOCATORS
        sub_topic_locators = STL.SUB_TOPIC_LOCATORS
        topic_links_locator = STL.LINK_FOOTER_SUBS
        for sub, top, link in zip(sub_locators, sub_topic_locators, topic_links_locator):
            self.el_click(sub)
            topics = self.el_get_all(top)
            links = self.el_get_all(link)
            for tpc, lnk in zip(topics, links):
                topic[tpc.text] = lnk.get_attribute('href')
        print(f'link sources: {topic}')
        return topic
