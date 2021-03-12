from selenium.webdriver.common.by import By


class StudentTutorLocators(object):
    
    
    
    # Locators for checking the presence of the element
    #Start Learning with Flexi
    
    TEXT_START_LEARN_FLEXI_HEAD = (By.XPATH, "//div[@class='feature-1-container subjects footer w-container']//div[@class='h3']")
    TEXT_START_LEARN_FLEXI_DESC = (By.XPATH, "//div[@class='feature-1-container subjects footer w-container']//div[@class='paragraph']")
    TEXT_BROWSE_ALL_FLEXBOOKS = (By.XPATH, "//a[@data-dx-desc='footer-subjects-browse-all-fbs']")
    #Teacher Banner
    BANNER_TEACHER = (By.XPATH, "//div[@class='remote-banner-bg']")
    TEXT_TEACHER_BANNER_HEAD = (By.XPATH, "//h1[@class='remote-banner-title']")
    TEXT_TEACHER_BANNER_DESC = (By.XPATH, "//p[@class='remote-banner-p']")
    TEXT_TEACHER_BANNER_TOUR = (By.XPATH, "//a[@data-dx-desc='footer-educator']")
    
    
    
    #Locators for checking the links
    
    LINK_TEACHER_BANNER_TOUR = (By.XPATH, "//a[@data-dx-desc='footer-educator']")
    LINK_BROWSE_ALL_FLEXBOOKS = (By.XPATH, "//a[@data-dx-desc='footer-subjects-browse-all-fbs']")
    LINK_START_LEARN_FLEXI_SCIENCE_TAB = (By.XPATH, "//a[@data-dx-desc='footer-subjects-science-tab']//div[contains(text(),'Science')]")
    LINK_START_LEARN_FLEXI_MATH_TAB = (By.XPATH, "//a[@data-dx-desc='footer-subjects-math-tab']//div[contains(text(),'Math')]")