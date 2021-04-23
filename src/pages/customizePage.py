from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeLocators as ALGEBRA
from locators.fb_math_algeb_8grade_locators import FBMathAlgeb8GradeCustomizeLocators as ALGEBRACUS
from pages.fbBrowseList_page import FbBrowseListPage
from selenium.webdriver import ActionChains


class CustomizePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def customTitle(self, text):
        self.el_click(ALGEBRA.LHS_CUSTOMIZE)
        self.el_send_keys(ALGEBRACUS.BOOK_TITLE_TEXT_FIELD, text)
        self.el_click(ALGEBRACUS.BOOK_TITLE_SAVE)
        self.pageTitle = self.el_get_text(ALGEBRA.FB_BOOK)
        print(f'From selectedBook page: {self.pageTitle}')

    def checkTitle(self, text):
        self.customTitle(text)
        return text == self.pageTitle

    def checkCreator(self, creator):
        self.created = self.el_get_text(ALGEBRA.FB_BOOK_CREATED_BY)
        print(f'Creator:{self.created}')
        return creator == self.created

    def checkDragDrop(self):
        chapters_list = self.el_get_all(ALGEBRACUS.CHAPTER_LIST)
        chapters = []
        for lists in chapters_list:
            chapters.append(lists.text)
        print(f'chapters: {chapters}')
        print(f'Dragged Chapter: {chapters[1]}')
        length = len(chapters)
        print(f'Total Chapters:{length}')
        if len(chapters) > 2:
            self.el_DragDrop(ALGEBRACUS.CHAP2_NAV_ICON,
                             ALGEBRACUS.CHAP4_NAV_ICON)
            time.sleep(5)
        else:
            print("Cannot perform drag and drop with single chapter")
        new_chapters_list = self.el_get_all(ALGEBRACUS.CHAPTER_LIST)
        new_chapters = []
        for lists in new_chapters_list:
            new_chapters.append(lists.text)
        print(f'New chapters: {new_chapters}')
        print(f'Dropped chapter: {new_chapters[3]}')
        return chapters[1] == new_chapters[3]

    def customChapTitle(self, text):
        self.el_click(ALGEBRACUS.CHAP1_EDIT_ICON)
        self.el_send_keys(ALGEBRACUS.EC_TITLE_TEXT, text)
        self.el_click(ALGEBRACUS.EC_DONE_BUTTON)
        Title = self.el_get_text(ALGEBRACUS.CHAP1_TITLE)
        print(f'Renamed Title: {Title}')
        return text == Title

    def addChapter(self, text):
        chapters_list = self.el_get_all(ALGEBRACUS.CHAPTER_LIST)
        chapters = []
        for lists in chapters_list:
            chapters.append(lists.text)
        print(f'chapters: {chapters}')
        length = len(chapters)-1
        print(f'Total Chapters:{length}')
        self.el_click(ALGEBRACUS.ADD_CHAP)
        self.el_send_keys(ALGEBRACUS.NC_TEXT, text)
        self.el_click(ALGEBRACUS.NC_DONE)
        time.sleep(5)
        new_chapters_list = self.el_get_all(ALGEBRACUS.CHAPTER_LIST)
        new_chapters = []
        for lists in new_chapters_list:
            new_chapters.append(lists.text)
        print(f'New chapters: {new_chapters}')
        new_length = len(new_chapters)-1
        print(f'New Length: {new_length}')
        added_chap = set(chapters).symmetric_difference(set(new_chapters))
        chapter_added = ''.join(added_chap)
        print(f'Newly Added Chapter: {chapter_added}')
        return text == chapter_added

    def removeChapter(self):
        chapters_list = self.el_get_all(ALGEBRACUS.CHAPTER_LIST)
        time.sleep(2)
        chapters = []
        for lists in chapters_list:
            chapters.append(lists.text)
        print(f'chapters: {chapters}')
        length = len(chapters)-1
        print(f'Total Chapters:{length}')
        chap_remove = chapters[0]
        print(f'Chapter to be removed: {chap_remove}')
        self.el_click(ALGEBRACUS.CHAP1_DELETE_ICON)
        self.el_click(ALGEBRACUS.REMOVE_BUTTON)
        time.sleep(5)
        new_chapters_list = self.el_get_all(ALGEBRACUS.CHAPTER_LIST)
        time.sleep(2)
        new_chapters = []
        for lists in new_chapters_list:
            new_chapters.append(lists.text)
        print(f'New chapters: {new_chapters}')
        new_length = len(new_chapters)-1
        print(f'New Length: {new_length}')
        removed_chap = set(new_chapters).symmetric_difference(set(chapters))
        chap_removed = ''.join(removed_chap)
        return length-1 == new_length

    def expandToggle(self):
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        Expanded = self.el_get(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_EXPANDED)
        if Expanded:
            all_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
            reads_list = []
            for lists in all_reads:
                reads_list.append(lists.text)
        print(f'Reads: {reads_list}')

    def checkReadDragDrop(self):
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        all_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        before_drop_reads = []
        for reads in all_reads:
            before_drop_reads.append(reads.text)
        print(f'Before Dropped: {before_drop_reads}')
        print(f'Dragged read: {before_drop_reads[1]}')
        length = len(before_drop_reads)

        if length > 2:
            self.el_DragDrop(ALGEBRACUS.R1_NAV_ICON, ALGEBRACUS.R5_NAV_ICON)
            time.sleep(6)
        else:
            print("Cannot perform drag and drop with single Read")

        all_reads_new = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        after_drop_reads = []

        for reads1 in all_reads_new:
            after_drop_reads.append(reads1.text)
        print(f'After Dropped: {after_drop_reads}')
        print(f'Dropped read: {after_drop_reads[5]}')
        return before_drop_reads[0] == after_drop_reads[4]

    def addRead(self, text):
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        all_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        before_add_reads = []
        for reads in all_reads:
            before_add_reads.append(reads.text)
        print(f'Before New Read Add: {before_add_reads}')
        self.el_click(ALGEBRACUS.CHAP1_ADD_READ)
        self.el_send_keys(ALGEBRACUS.TEXT_FIELD, text)
        self.el_click(ALGEBRACUS.DONE_BUTTON)

        all_reads_new = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        after_add_reads = []

        for reads1 in all_reads_new:
            after_add_reads.append(reads1.text)
        print(f'After New read added: {after_add_reads}')
        new_added = set(after_add_reads).symmetric_difference(
            set(before_add_reads))
        new_read = ''.join(new_added)
        return text == new_read

    def collectDDList(self):
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        self.el_click(ALGEBRACUS.R1_ELLIPSIS_ICON)
        time.sleep(3)
        ddList = self.el_get_all(ALGEBRACUS.R1_ELLIPSIS_DD_LIST1)
        dropDown_List = []
        for lists in ddList:
            dropDown_List.append(lists.text)
        print(f'List Drop Down: {dropDown_List}')
        print(len(dropDown_List))
        return len(dropDown_List) == 6

    def removeRead(self):
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        all_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        before_remove_reads = []
        for reads in all_reads:
            before_remove_reads.append(reads.text)
        print(f'Before Read Removed: {before_remove_reads}')
        length = len(before_remove_reads)
        self.selectItem(ALGEBRACUS.R1_ELLIPSIS_ICON, ALGEBRACUS.R1_DD_REMOVE)
        self.el_click(ALGEBRACUS.REMOVE_BUTTON)
        all_reads_new = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        after_remove_reads = []
        for reads1 in all_reads_new:
            after_remove_reads.append(reads1.text)
        print(f'After read removed: {after_remove_reads}')
        newLength = len(after_remove_reads)
        return newLength == length-1

    def renameRead(self, text):
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        self.selectItem(ALGEBRACUS.R1_ELLIPSIS_ICON, ALGEBRACUS.R1_DD_RENAME)
        self.el_click(ALGEBRACUS.RRW_CONTINUE_BUTTON)
        self.el_send_keys(ALGEBRACUS.TEXT_FIELD, text)
        self.el_click(ALGEBRACUS.DONE_BUTTON)
        new_Title = self.el_get_text(ALGEBRACUS.R1_TITLE_NAME)
        return text == new_Title

    def move_read_diff_chap(self):
        chap1 = []
        chap5 = []
        new_chap1 = []
        new_chap5 = []
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        chap1_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        for chap1_read in chap1_reads:
            chap1.append(chap1_read.text)
        print(f'chap1: {chap1}')

        chap5_toggle = self.el_get(ALGEBRACUS.CHAP5_EXPAND_TOGGLE)
        action = ActionChains(self.driver)
        action.move_to_element(chap5_toggle)
        chap5_toggle.click()
        chap5_reads = self.el_get_all(ALGEBRACUS.CHAP5_EXPAND_ALL_READS)
        for chap5_read in chap5_reads:
            chap5.append(chap5_read.text)
        print(f'chap5: {chap5}')

        action.move_to_element(self.el_present(
            ALGEBRACUS.R1_NAV_ICON))

        self.el_DragDrop(ALGEBRACUS.C1R1, ALGEBRACUS.C5R1)
        time.sleep(2)
        new_chap5_reads = self.el_get_all(ALGEBRACUS.CHAP5_EXPAND_ALL_READS)
        time.sleep(1)
        for new_chap5_read in new_chap5_reads:
            new_chap5.append(new_chap5_read.text)
        print(f'new chap5: {new_chap5}')
        self.el_click(ALGEBRACUS.CHAP5_EXPAND_TOGGLE_EXPANDED)
        action.move_to_element(self.el_get(ALGEBRACUS.R1_NAV_ICON))
        new_c1_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        for new_c1_read in new_c1_reads:
            new_chap1.append(new_c1_read.text)
        print(f'new chap1: {new_chap1}')
        removed_read_c1 = set(chap1).symmetric_difference(set(new_chap1))
        print(f'Removed from Chap 1: {removed_read_c1}')
        added_read_c5 = set(new_chap5).symmetric_difference(set(chap5))
        print(f'Added in Chapter 5: {added_read_c5}')
        return removed_read_c1 == added_read_c5

    def move_to_dropDown(self):
        chap1 = []
        chap5 = []
        new_chap1 = []
        new_chap5 = []
        self.el_click(ALGEBRACUS.CHAP1_EXPAND_TOGGLE_HIDDEN)
        chap1_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        for chap1_read in chap1_reads:
            chap1.append(chap1_read.text)
        print(f'chap1: {chap1}')

        chap5_toggle = self.el_get(ALGEBRACUS.CHAP5_EXPAND_TOGGLE)
        action = ActionChains(self.driver)
        action.move_to_element(chap5_toggle)
        chap5_toggle.click()
        chap5_reads = self.el_get_all(ALGEBRACUS.CHAP5_EXPAND_ALL_READS)
        for chap5_read in chap5_reads:
            chap5.append(chap5_read.text)
        print(f'chap5: {chap5}')
        time.sleep(2)
        action.move_to_element(self.el_get(
            ALGEBRACUS.R1_ELLIPSIS_ICON))
        time.sleep(1)
        self.el_click(ALGEBRACUS.R1_ELLIPSIS_ICON)
        self.el_click(ALGEBRACUS.R1_DD_MV)
        action.move_to_element(self.el_present(ALGEBRACUS.R1_MV_DD_R5))
        self.el_click(ALGEBRACUS.R1_MV_DD_R5)
        time.sleep(2)

        new_chap5_reads = self.el_get_all(ALGEBRACUS.CHAP5_EXPAND_ALL_READS)
        time.sleep(1)
        for new_chap5_read in new_chap5_reads:
            new_chap5.append(new_chap5_read.text)
        print(f'new chap5: {new_chap5}')

        ActionChains(self.driver).move_to_element(
            self.el_get(ALGEBRACUS.CHAP5_INDEX)).perform()
        self.el_click(ALGEBRACUS.CHAP5_EXPAND_TOGGLE_EXPANDED)

        ActionChains(self.driver).move_to_element(
            self.el_get(ALGEBRACUS.R1_NAV_ICON)).perform()
        new_c1_reads = self.el_get_all(ALGEBRACUS.CHAP1_EXPAND_ALL_READS)
        for new_c1_read in new_c1_reads:
            new_chap1.append(new_c1_read.text)
        print(f'new chap1: {new_chap1}')

        removed_read_c1 = set(chap1).symmetric_difference(set(new_chap1))
        print(f'Removed from Chap 1: {removed_read_c1}')
        added_read_c5 = set(new_chap5).symmetric_difference(set(chap5))
        print(f'Added in Chapter 5: {added_read_c5}')
        return removed_read_c1 == added_read_c5
