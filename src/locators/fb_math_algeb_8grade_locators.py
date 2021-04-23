from selenium.webdriver.common.by import By


# Create class for ck-12 Middle School Math Concept-Grade 8
class FBMathAlgeb8GradeLocators(object):
    # ck-12 Middle School Math Concept-Grade 8 locator in Algebra page
    FB_MATH_ALGEBRA_8GRADE = (
        By.XPATH, "//a[normalize-space()='CK-12 Middle School Math Concepts - Grade 8']")
    #  in book page
    FB_BOOK = (By.CSS_SELECTOR, "h1:nth-child(1) > span")
    # Created By
    FB_BOOK_CREATED_BY = (
        By.XPATH, "//span[normalize-space()='Created by:']/following-sibling::span")
    # LHS Menu locators
    LHS_ADD_TO_LIBRARY = (By.XPATH, "//a[contains(text(),'Add to Library')]")
    LHS_SHARE_WITH_CLASSES = (
        By.XPATH, "//a[contains(text(),'Share with Classes')]")
    LHS_ADD_TO_FB_TEXTBOOK = (
        By.XPATH, "//a[contains(text(),'Add to FlexBook® Textbook')]")
    LHS_CUSTOMIZE = (By.XPATH, "//a[normalize-space()='Customize']")
    LHS_CUSTOMIZE_HELP = (
        By.XPATH, "//body/div[@id='content-container']/div[@id='flexBookDetailsMain']/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[4]/span[1]/div[1]/span[1]/a[1]")
    LHS_OFFLINE_READER = (By.XPATH, "//a[contains(text(),'Offline Reader')]")
    LHS_OFFLINE_READER_HELP = (By.XPATH, "//span[@id='tt-offlineReader']")

    # Menu above table of content locators
    READ_BUTTON = (By.XPATH, "//button[@id='tab-tab_content']")
    RESOURCES_BUTTON = (By.XPATH, "//button[@id='tab-tab_resources']")
    DETAILS_BUTTON = (By.XPATH, "//button[@id='tab-tab_details']")

    # Table of content text locators
    TABLE_OF_CONTENT_TEXT = (
        By.XPATH, "//div[contains(text(),'Table of Contents')]")

    # Read-Table of content of ck-12 Middle School Math Concept-Grade 8 locators

# A class created for customize page of the book


class FBMathAlgeb8GradeCustomizeLocators(object):
    # Book Title customize locator
    BOOK_TITLE_TEXT_FIELD = (By.XPATH, "//input[@id='txt_artifacttitle']")
    BOOK_TITLE_SAVE = (By.XPATH, "//a[@id='btn_save_artifact']")

    # Locators for edit page
    EDIT = (By.CSS_SELECTOR, "#ui-id-2")
    TOC_TEXT1 = (By.XPATH, "//h2[contains(text(),'Table of Content')]")

    # ?Locators to add chapter, new read, or search library
    ADD_CHAP = (By.XPATH, "(//a[contains(@class,'new_chapter_inline')])[1]")
    ADD_NEW_READ = (
        By.XPATH, "//body/div[@id='content-container']/div[@id='contentwrap']/div[@id='content']/article[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]")
    SEARCH_FROM_CK12LIBRARY = (By.CSS_SELECTOR, "div.container_12.clearfix:nth-child(6) div.clearfix.grid_10 div.js_editortabs.ui-tabs.ui-widget.ui-widget-content.ui-corner-all div.contentarea div.contentview.js_viewtab.ui-tabs-panel.ui-widget-content.ui-corner-bottom div.clearfix div.js_detailbody.js_book_editor div.book_editor_title:nth-child(1) div.editor_add_more.editor_add_more--top.hide-for-collaborator:nth-child(2) > a.search_inline")
    # ?Locatorsto add text inside new chapter text field @ NC_TEXT and save @NC_DONE
    NC_TEXT = (By.XPATH, "//input[@placeholder='Chapter Name']")
    NC_DONE = (By.XPATH, "//button[normalize-space()='Done']")
    # ?Locators of remove, and cancel button inside delete chapter, read Modal
    REMOVE_BUTTON = (By.XPATH, "//div[normalize-space()='Remove']")
    CANCEL_BUTTON = (By.XPATH, "//div[normalize-space()='Cancel']")
    # ?Locators of edit chapter modal @EC
    # Locators inside basic information tab
    EC_TITLE_TEXT = (By.XPATH, "//input[@id='txt_chapter_title']")
    EC_DESC_TEXT = (By.XPATH, "//textarea[@id='txt_chapter_desc']")

    EC_DONE_BUTTON = (By.XPATH, "//input[@id='js_savechapter']")

    # ? Chapters list- locator for all chapter
    CHAPTER_LIST = (
        By.XPATH, "//li//div[1]//div[1]//span[3]/preceding-sibling::span[1]")
    # ?List of chapter names with class name
    CHAP_LIST = (By.CLASS_NAME, "row_artifact_title js_artifact_title")
    # ?Edit/Rename, or addition of chapters, reads - text and done locators
    TEXT_FIELD = (By.XPATH, "//input[@placeholder='Section Name']")
    DONE_BUTTON = (By.XPATH, "//button[@id='js_row_lesson_save']")
    # ?Chapters edit, navigate, delete locators

    # ?Chapter1 edit, navigate,detele locators
    CHAP1_TITLE = (
        By.XPATH, "//li[1]//div[1]//div[1]//span[4]/preceding-sibling::span[2]")
    CHAP1_EDIT_ICON = (
        By.XPATH, "//li[1]//div[1]//div[1]//div[2]//a[3]")
    CHAP1_DELETE_ICON = (
        By.XPATH, "//li[1]//div[1]//div[1]//div[2]//a[2]//span[1]")
    CHAP1_NAV_ICON = (
        By.XPATH, "//li[1]//div[1]//div[1]//div[2]//a[1]//span[1]")
    CHAP1_ADD_READ = (By.XPATH, "(//a[contains(text(),'New Read')])[2]")

    # ?Chapter2 edit, navigate, delete locators
    CHAP2_EDIT_ICON = (
        By.XPATH, "//li[2]//div[1]//div[1]//div[2]//a[3]//span[1]")
    CHAP2_DELETE_ICON = (
        By.XPATH, "//li[2]//div[1]//div[1]//div[2]//a[2]//span[1]")
    CHAP2_NAV_ICON = (
        By.XPATH, "//li[2]//div[1]//div[1]//div[2]//a[1]//span[1]")
    # ?Chapter3 edit, navigate, delete locators
    CHAP3_EDIT_ICON = (
        By.XPATH, "//li[3]//div[1]//div[1]//div[2]//a[3]//span[1]")
    CHAP3_DELETE_ICON = (
        By.XPATH, "//li[3]//div[1]//div[1]//div[2]//a[2]//span[1]")
    CHAP3_NAV_ICON = (
        By.XPATH, "//li[3]//div[1]//div[1]//div[2]//a[1]//span[1]")
    CHAP3_TITLE_NAME = (By.XPATH, "//body/div[@id='content-container']/div[@id='contentwrap']/div[@id='content']/article/div[@id='editor_container']/div[@id='editor_tabs']/div[contains(@class,'contentarea')]/div[@id='edit_content']/div[@id='artifact_content']/div[contains(@class,'js_detailbody js_book_editor')]/div[@id='chapter_list']/ul[contains(@class,'chapterlist js_artifact_list modified ui-sortable')]/li[3]/div[1]/div[1]")
    CHAP3_INDEX = (
        By.XPATH, "//span[@class='index_label js_index_label child'][normalize-space()='3']")
    # ?Chapter4 edit, navigate, delete locators
    CHAP4_EDIT_ICON = (
        By.XPATH, "//li[4]//div[1]//div[1]//div[2]//a[3]//span[1]")
    CHAP4_DELETE_ICON = (
        By.XPATH, "//li[4]//div[1]//div[1]//div[2]//a[2]//span[1]")
    CHAP4_NAV_ICON = (
        By.XPATH, "//li[4]//div[1]//div[1]//div[2]//a[1]//span[1]")
    CHAP4_INDEX = (
        By.XPATH, "//span[@class='index_label js_index_label child'][normalize-space()='4']")
    CHAP4_TITLE_NAME = (By.XPATH, "//body/div[@id='content-container']/div[@id='contentwrap']/div[@id='content']/article/div[@id='editor_container']/div[@id='editor_tabs']/div[contains(@class,'contentarea')]/div[@id='edit_content']/div[@id='artifact_content']/div[contains(@class,'js_detailbody js_book_editor')]/div[@id='chapter_list']/ul[contains(@class,'chapterlist js_artifact_list modified ui-sortable')]/li[4]/div[1]/div[1]")
    # ?Chapter5 edit, navigate, delete locators
    CHAP5_EDIT_ICON = (
        By.XPATH, "//li[5]//div[1]//div[1]//div[2]//a[3]//span[1]")
    CHAP5_DELETE_ICON = (
        By.XPATH, "//li[5]//div[1]//div[1]//div[2]//a[2]//span[1]")
    CHAP5_NAV_ICON = (
        By.XPATH, "//li[5]//div[1]//div[1]//div[2]//a[1]//span[1]")
    CHAP5_INDEX = (
        By.XPATH, "//span[@class='index_label js_index_label child'][normalize-space()='5']")
    # ?Chapter1 Expand toggle in edit page locators
    CHAP1_EXPAND_TOGGLE_HIDDEN = (
        By.XPATH, "(//div[@class='js_expand_toggle row_expand_toggle ui-icon ui-icon-triangle-1-e'])[1]")
    CHAP1_EXPAND_TOGGLE_EXPANDED = (
        By.XPATH, "(//div[@class='js_expand_toggle row_expand_toggle ui-icon ui-icon-triangle-1-s'])[1]")
    CHAP1_EXPAND_ALL_READS = (
        By.XPATH, "//div[@class='editor_chapterinfo']/ul/li/div/div/div[2]/span[1]")
    CHAP1_EXPAND_STATUS = (
        By.XPATH, "//div[@class='js_expand_toggle row_expand_toggle ui-icon ui-icon-triangle-1-s']")

    # ?Chapter5 Expand Toggle in edit page locators
    CHAP5_EXPAND_TOGGLE = (
        By.XPATH, "(//div[@class='js_expand_toggle row_expand_toggle ui-icon ui-icon-triangle-1-e'])[4]")
    CHAP5_EXPAND_TOGGLE_EXPANDED = (
        By.XPATH, "(//div[@class='js_expand_toggle row_expand_toggle ui-icon ui-icon-triangle-1-s'])[2]")
    CHAP5_EXPAND_ALL_READS = (
        By.XPATH, "//div[@id='chapter_list']/descendant::li[1]/following-sibling::li[4]/descendant::div[7]/child::ul/li/div/div/div/span[1]")

    # ?All Chapter expand Toggle-hidden
    CH1_TOGGLE_HIDDEN = (
        By.XPATH, "//li[@class='ui-corner-all artifact_type_chapter js_artifact_list_item ui-droppable loaded']//div[@class='row_expand_toggle_parent js-expand-toggle']")

    # ?Reads Rename warning modal locators @ RRW
    RRW_CONTINUE_BUTTON = (By.XPATH, "//div[contains(text(),'Continue')]")
    RRW_CANCEL_BUTTON = (By.XPATH, "//div[contains(text(),'Cancel')]")

    # ?Read1 @ R1 locators

    R1_NAV_ICON = (
        By.XPATH, "//li[@class='ui-corner-all artifact_type_chapter js_artifact_list_item ui-droppable loaded']//li[1]//div[1]//div[1]//div[3]//a[2]")
    R1_ELLIPSIS_ICON = (
        By.XPATH, "(//div[@class='editor_chapterinfo'])[1]/descendant::li[1]/descendant::div[5]/descendant::a[1]")
    R1_TITLE_NAME = (By.XPATH, "(//span[@class='draft-chapter-title'])[1]")
    R1_ELLIPSIS_DD_LIST = (
        By.XPATH, "//div[contains(@class,'more-options-dropdown-wrapper user_more_options open')]/div/ul[1]/li/a/span")
    R1_ELLIPSIS_DD_LIST1 = (
        By.XPATH, "//div[contains(@class,'more-options-dropdown-wrapper user_more_options open')]//ul[contains(@class,'more-options-dropdown')]//li//a//span[1]")
    R1_MV_DD_R2 = (
        By.XPATH, "//div[contains(@class,'more-options-dropdown-wrapper user_more_options open show-chapter-list')]/div/div/ul/li[1]/a")
    R1_MV_DD_R5 = (
        By.XPATH, "//div[contains(@class,'more-options-dropdown-wrapper user_more_options open show-chapter-list')]/div/div/ul/li[4]/a")

    # ?Read5 @ R5 locators
    R5_NAV_ICON = (By.XPATH, "//li[5]//div[1]//div[1]//div[3]//a[2]//span[1]")

    # ?Chap1 Read 1 and Chap5 Read1
    C1R1 = (
        By.XPATH, "(//ul[@class='conceptlist child js_artifact_list ui-sortable']/li[1]//a[@title='Rearrange'])[1]")
    C5R1 = (
        By.XPATH, "(//ul[@class='conceptlist child js_artifact_list ui-sortable']/li[1]//a[@title='Rearrange'])[2]")
    # ?R1 Ellipsis dropdown@DD list
    R1_DD_EDIT = (
        By.XPATH, "//div[@class='more-options-dropdown-wrapper user_more_options open']//a[@title='Edit']")
    R1_DD_RENAME = (
        By.XPATH, "//div[@class='more-options-dropdown-wrapper user_more_options open']//span[contains(text(),'Rename')]")
    R1_DD_MV = (
        By.XPATH, "//div[@class='more-options-dropdown-wrapper user_more_options open']//span[contains(text(),'Move To')]")
    R1_MV_ARROW_ICON = (
        By.XPATH, "//div[@class='more-options-dropdown-wrapper user_more_options open']//span[@class='icon-play']")
    R1_DD_REMOVE = (
        By.XPATH, "//div[@class='more-options-dropdown-wrapper user_more_options open']//a[@title='Remove']")
    # ?R1 TITLE Edit page locators
    R1_TITLE_FIELD = (By.XPATH, "//input[@id='txt_artifacttitle']")
    R1_TITLE_SAVE_BUTTON = (By.XPATH, "//a[@id='new-modality-save']")
    R1_TITLE_SAVED_STATUS = (By.XPATH, "//a[contains(text(),'Saved!')]")
    R1_TITLE_GOBACK_BUTTON = (
        By.XPATH, "//header/div[@id='new-modality-save-container']/a[2]")
    # ?R1 Content EdiT page locators
    R1CONT_EDIT_TEXT = (By.CSS_SELECTOR, "#ui-id-2")
    MCE_EDITOR_MENU = (By.ID, "mceu_31-body")
    # Locators for resources page
    RESOURCES = (By.CSS_SELECTOR, "#ui-id-3")

    # Locators for details page
    DETAILS = (By.CSS_SELECTOR, "#ui-id-4")
