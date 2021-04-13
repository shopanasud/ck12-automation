import time
import unittest

import pytest
from locators.studentTutorLocators import StudentTutorLocators as STL
from pages.basePage import BasePage
from pages.studentTutorPage import StudentTutorPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class testStudentTutor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://www.ck12.org/pages/student-tutor/')
        close = StudentTutorPage(self.driver)
        close.close_banner()

    # Test the title of the page
    def test_TC001_pageTitle(self):
        actual = self.driver.title
        expected = STL.STUDENT_TUTOR
        self.assertEqual(actual, expected)

    # Test case to check All the headings present in the page.

    def test_TC002_text_check_headings(self):
        heading = StudentTutorPage(self.driver)
        actual_Headings = heading.get_HeadingTitle()
        expected_Headings = STL.HEADERS
        for head in actual_Headings:
            self.assertIn(head, expected_Headings)

    # Test case to check all available text present in the page.
    def test_TC003_text_all_available_element(self):
        para = StudentTutorPage(self.driver)
        actual_content = para.get_AllText()
        expected_content = STL.AVAILABLE_TEXT
        for txt in actual_content:
            self.assertIn(txt, expected_content)

    # Test case to check the Subject names in the footer.
    def test_TC004_text_subNames(self):
        sub = StudentTutorPage(self.driver)
        expected_list = STL.SUBJECTS
        print(f'Expected: {expected_list}')
        actual_list = sub.get_Subjects()
        assert actual_list == expected_list

    # Test case to check the text present in the Testimonial (Carousal)
    def test_TC005_text_testimonial(self):
        testimonial = StudentTutorPage(self.driver)
        actual_testimonial_txt = testimonial.get_Testimonials_text()
        expected_testimonial_txt = STL.TESTIMONIAL_TEXT
        for txt in actual_testimonial_txt:
            self.assertIn(txt, expected_testimonial_txt)

    # Test case to check the Topics text inside each subjects.
    def test_TC006_text_checkTopics(self):
        sub_topic = BasePage(self.driver)
        sub_list = STL.SUBJECTS
        sub_locators = STL.SUBJECTS_LOCATORS
        sub_topic_locators = STL.SUB_TOPIC_LOCATORS
        for i, j, k in zip(sub_list, sub_locators, sub_topic_locators):
            sub_topic.el_click(j)
            print(f'{i} Subject Clicked')
            topic = []
            topics = sub_topic.el_get_all(k)
            for m in topics:
                topic.append(m.text)
            print(f'{i} : {topic}')
            if i == 'SCIENCE':
                assert topic == STL.SCIENCE_TOPICS
                print('Science topics matches with the actual.')
            elif i == 'MATH':
                assert topic == STL.MATH_TOPICS
                print('Math topics matches with the actual.')
            else:
                return False

    # Test case to check the available text in the modal- subject
    def test_TC007_text_in_modal(self):
        modal = StudentTutorPage(self.driver)
        actual_modal_text = modal.get_ModalText()
        expected_modal_text = STL.MODAL_WIN_TEXT
        for txt in actual_modal_text:
            self.assertIn(txt, expected_modal_text)

    # Test case to check the Subject names present in the modal .
    def test_TC008_text_modalSubNames(self):
        sub = StudentTutorPage(self.driver)
        expected_list = STL.SUBJECTS
        print(f'Expected: {expected_list}')
        actual_list_modal = sub.get_ModalSubjects()
        assert actual_list_modal == expected_list

    # Test case to check the Topics text inside each subjects in the modal.
    def test_TC009_text_modalCheckTopic(self):
        subjects = StudentTutorPage(self.driver)
        sub_list = subjects.get_ModalSubjects()
        sub_topic = BasePage(self.driver)
        sub_locators = STL.MODAL_SUB_LOCATORS
        sub_topic_locators = STL.MODAL_SUB_TOPIC_LOCATORS
        for i, j, k in zip(sub_list, sub_locators, sub_topic_locators):
            sub_topic.el_click(j)
            print(f'{i} Subject Clicked')
            topic = []
            topics = sub_topic.el_get_all(k)
            for m in topics:
                topic.append(m.text)
            print(f'{i} : {topic}')
            if i == 'SCIENCE':
                assert topic == STL.SCIENCE_TOPICS
                print('Science topics matches with the actual.')
            elif i == 'MATH':
                assert topic == STL.MATH_TOPICS
                print('Math topics matches with the actual.')
            else:
                return False

    # Test case to check the links of the Topics in the modal.
    def test_TC010_link_modalCheckTopicTitles(self):
        title = StudentTutorPage(self.driver)
        title_list_actual = title.get_ModalTopicTitle()
        title_list_expected = STL.TOPICS_TITLE
        self.assertEqual(title_list_actual, title_list_expected)

    # test case to check the link of Browse All Flexbook in the modal.
    def test_TC011_link_modalBrowseAllTitle(self):
        title = StudentTutorPage(self.driver)
        actual_title = title.check_ModalBrowseAll()
        expected_title = STL.BROWSE_ALL_FLEX
        self.assertEqual(actual_title, expected_title)

    # Test case to check the subject topic links present in the footer.
    def test_TC012_link_CheckTopicTitles(self):
        title = StudentTutorPage(self.driver)
        title_list_actual = title.get_TopicTitle()
        title_list_expected = STL.TOPICS_TITLE
        self.assertEqual(title_list_actual, title_list_expected)

    # Test case to check the links of signup and Teacher Tutor page.
    def test_TC013_link_OtherPageTitles(self):
        title = StudentTutorPage(self.driver)
        actual_title = title.get_PageTitles()
        expected_title = STL.PAGE_TITLES
        for title in actual_title:
            self.assertIn(title, expected_title)

    # Test case to chec the images of the topics present in the Footer subjects
    def test_TC014_imagePresence_sub(self):
        image = StudentTutorPage(self.driver)
        actual = image.check_imagePresence_sub()
        expected = STL.IMAGE_SOURCE
        for each in actual:
            self.assertIn(each, expected)

    # Test case to check all the available images present in the page.
    def test_TC0015_imagePresence(self):
        image = StudentTutorPage(self.driver)
        actual = image.check_ImagePresence()
        expected = STL.IMAGE_SOURCE
        for each in actual:
            self.assertIn(each, expected)

    # Test case to check the topics image present in the modal.
    def test_TC0016_imagePresence_modalSub(self):
        image = StudentTutorPage(self.driver)
        actual = image.check_imagePresence_sub_modal()
        expected = STL.IMAGE_SOURCE
        for each in actual:
            self.assertIn(each, expected)

    # Test case to check the user image present in the Testimonials.
    def test_TC0017_ImagePresence_testimonial(self):
        image = StudentTutorPage(self.driver)
        actual = image.check_testimonialImage()
        expected = STL.IMAGE_SOURCE
        for each in actual:
            self.assertIn(each, expected)

    # Test case to check the links present in the modal
    def test_TC018_linkSource_modal(self):
        source = StudentTutorPage(self.driver)
        actual = source.get_linkSource_modal()
        expected = STL.LINKS_AVAILABLE
        for src in actual:
            self.assertIn(src, expected)

    # Test case to check the links present in the page
    def test_TC019_linkSource(self):
        source = StudentTutorPage(self.driver)
        actual = source.get_linkSource()
        expected = STL.LINKS_AVAILABLE
        for src in actual:
            self.assertIn(src, expected)

     # Test case to check the Broken links present in the DOM.
    def test_TC020_brokenLinks(self):
        broken_links = StudentTutorPage(self.driver)
        listed = broken_links.get_brokenLinks()
        self.assertEqual(len(listed), 0)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
