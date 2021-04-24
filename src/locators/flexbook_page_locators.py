from selenium.webdriver.common.by import By

# A Class for Flexbook page locators


class FlexbookPageLocators(object):

    TEXT_AVAILABLE = {'Tag': 'Customizable digital textbooks',
                      'Description': 'CK-12 FlexBooks® are fully customizable, digital textbooks which offer the best content for students and teachers. Viewable on Chromebooks, laptops, tablets, smartphones or desktops, FlexBooks® are standards-aligned and ready to be localized to engage students.',
                      'Language': 'All Languages',
                      'Subjects': 'All Subjects',
                      'Grades': 'All Grades',
                      'Search': 'Search FlexBooks®'}
    OPTIONS_TXT = {'Languages': ['All Languages', 'English', 'Spanish'],
                   'Subjects': ['All Subjects', 'Math', '    Algebra', '    Arithmetic', '    Measurement', '    Geometry', '    Probability', '    Statistics', '    Trigonometry', '    Analysis', '    Calculus', 'Science', '    Elementary Science', '    Earth Science', '    Life Science', '    Physical Science', '    Biology',
                                '    Chemistry', '    Physics', '    Engineering', '    Technology', '    Astronomy', '    Health', 'Language Arts', '    Writing', '    Spelling', 'Photography', '    Photography', 'Social Studies', '    Economics', '    Geography', '    Government', '    History', '    Philosophy', '    Sociology'],
                   'Grades': ['All Grades', 'Middle School', 'High School', 'Elementary School']}
    IMAGE_SRC = {'Head_Text_FB': 'https://www.ck12info.org/about/wp-content/uploads/2018/05/Screen-Shot-2018-05-31-at-9.02.06-PM.png',
                 'Container_Text_FB': 'https://www.ck12info.org/about/wp-content/uploads/2018/06/flexlogo.jpg',
                 'Container_Image_FB': 'https://www.ck12info.org/about/wp-content/uploads/2018/06/book.jpg'}
    # FLEXBOOK landing page locators
    FB_EXPLORE_MENU = (By.XPATH, "//header/nav[1]/section[1]/ul[1]/li[5]/a[1]")
    FB_FLEXBOOK_OPTION = (
        By.XPATH, "//section[@class='sc-kafWEX bnzRUy']//div[@class='item-title sc-kgAjT jfQxeN'][normalize-space()='FlexBooks®']")
    # Flexbook page
    FB_PAGE_TITLE = (
        By.XPATH, "//title[contains(text(),'FlexBooks® | CK-12 Foundation')]")
    FB_BANNER_TEXT = (
        By.XPATH, "//span[contains(text(),'Customizable digital textbooks')]")

    # Language selection locators
    FB_LANGUAGE_DROPDOWN = (By.XPATH, "//select[@name='Language']")
    FB_LANGUAGE_ALLLANGUAGE = (
        By.XPATH, "//option[contains(text(),'All Languages')]")
    FB_LANGUAGE_ENGLISH = (By.XPATH, "//option[contains(text(),'English')]")
    FB_LANGUAGE_SPANISH = (By.XPATH, "//option[contains(text(),'Spanish')]")

    # Subject Selection Locators
    FB_SUBJECT_DROPDOWN = (By.NAME, "Subject")
    FB_SUBJECT_ALLSUBJCTS = (
        By.XPATH, "//option[contains(text(),'All Subjects')]")
    # Maths locators
    FB_SUBJECTS_MATH = (By.XPATH, "//option[contains(text(),'Math')]")
    FB_SUBJECTS_MATH_ALGEBRA = (
        By.XPATH, "//option[contains(text(),'Algebra')]")
    FB_SUBJECTS_MATH_ARITHMATIC = (
        By.XPATH, "//option[contains(text(),'Arithmetic')]")
    FB_SUBJECTS_MATH_MEASUREMENT = (
        By.XPATH, "//option[contains(text(),'Measurement')]")
    FB_SUBJECTS_MATH_GEOMETRY = (
        By.XPATH, "//option[contains(text(),'Geometry')]")
    FB_SUBJECTS_MATH_PROBABILITY = (
        By.XPATH, "//option[contains(text(),'Probability')]")
    FB_SUBJECTS_MATH_STATISTICS = (
        By.XPATH, "//option[contains(text(),'Statistics')]")
    FB_SUBJECTS_MATH_TRIGNOMETRY = (
        By.XPATH, "//option[contains(text(),'Trigonometry')]")
    FB_SUBJECTS_MATH_ANALYSIS = (
        By.XPATH, "//option[contains(text(),'Analysis')]")
    FB_SUBJECTS_MATH_CALCULUS = (
        By.XPATH, "//option[contains(text(),'Calculus')]")
    # Science locators
    FB_SUBJECTS_SCIENCE = (
        By.XPATH, "//body/div[@id='fbbrowse-root']/div[1]/div[2]/div[1]/div[2]/div[3]/select[2]/option[12]")
    FB_SUBJECTS_SCIENCE_ELEMENTARYSCIENCE = (
        By.XPATH, "//option[contains(text(),'Elementary Science')]")
    FB_SUBJECTS_SCIENCE_EARTHSCIENCE = (
        By.XPATH, "//option[contains(text(),'Earth Science')]")
    FB_SUBJECTS_SCIENCE_LIFESCIENCE = (
        By.XPATH, "//option[contains(text(),'Life Science')]")
    FB_SUBJECTS_SCIENCE_PHYSICALSCIENCE = (
        By.XPATH, "//option[contains(text(),'Physical Science')]")
    FB_SUBJECTS_SCIENCE_BIOLOGY = (
        By.XPATH, "//option[contains(text(),'Biology')]")
    FB_SUBJECTS_SCIENCE_CHEMISTRY = (
        By.XPATH, "//option[contains(text(),'Chemistry')]")
    FB_SUBJECTS_SCIENCE_PHYSICS = (
        By.XPATH, "//option[contains(text(),'Physics')]")
    FB_SUBJECTS_SCIENCE_ENGINEERING = (
        By.XPATH, "//option[contains(text(),'Engineering')]")
    FB_SUBJECTS_SCIENCE_TECHNOLOGY = (
        By.XPATH, "//option[contains(text(),'Technology')]")
    FB_SUBJECTS_SCIENCE_ASTRONOMY = (
        By.XPATH, "//option[contains(text(),'Astronomy')]")
    FB_SUBJECTS_SCIENCE_HEALTH = (
        By.XPATH, "//option[contains(text(),'Health')]")
    # Language Arts locators
    FB_SUBJECTS_LANGUAGEARTS = (
        By.XPATH, "//option[contains(text(),'Language Arts')]")
    FB_SUBJECTS_LANGUAGEARTS_WRITING = (
        By.XPATH, "//option[contains(text(),'Writing')]")
    FB_SUBJECTS_LANGUAGEARTS_SPELLING = (
        By.XPATH, "//option[contains(text(),'Spelling')]")
    # Photography locators
    FB_SUBJECTS_PHOTOGRAPHY = (
        By.XPATH, "//body/div[@id='fbbrowse-root']/div[1]/div[2]/div[1]/div[2]/div[3]/select[2]/option[28]")
    # Social Studies locators
    FB_SUBJECTS_SOCIAL_ECONOMICS = (
        By.XPATH, "//option[contains(text(),'Economics')]")
    FB_SUBJECTS_SOCIAL_GEOGRAPHY = (
        By.XPATH, "//option[contains(text(),'Geography')]")
    FB_SUBJECTS_SOCIAL_GOVERNMENT = (
        By.XPATH, "//option[contains(text(),'Government')]")
    FB_SUBJECTS_SOCIAL_HISTORY = (
        By.XPATH, "//option[contains(text(),'History')]")
    FB_SUBJECTS_SOCIAL_PHILOSOPHY = (
        By.XPATH, "//option[contains(text(),'Philosophy')]")
    FB_SUBJECTS_SOCIAL_SOCIOLOGY = (
        By.XPATH, "//option[contains(text(),'Sociology')]")

    # Grades locators
    FB_GRADES_DROPDOWN = (
        By.XPATH, "//body/div[@id='fbbrowse-root']/div[1]/div[2]/div[1]/div[2]/div[3]/select[3]")
    FB_GRADES_ALLGRADES = (By.XPATH, "//option[contains(text(),'All Grades')]")
    FB_GRADES_MIDDLE = (By.XPATH, "//option[contains(text(),'Middle School')]")
    FB_GRADES_HIGH = (By.XPATH, "//option[contains(text(),'High School')]")
    FB_GRADES_ELEMENTARY = (
        By.XPATH, "//option[contains(text(),'Elementary School')]")

    # Search button locator
    FB_SEARCH = (By.XPATH, "//div[contains(text(),'Search FlexBooks®')]")

    TEXT = {
        "Tag": (By.XPATH, "//span[contains(@class,'bannercomponent')]"),
        "Description": (By.XPATH, "//p[contains(@class,'descriptioncomponent')]"),
        "Language": (By.XPATH, "//select[@name='Language']/option[1]"),
        "Subjects": (By.XPATH, "//select[@name='Subject']/option[1]"),
        "Grades": (By.XPATH, "//select[@name='Grade']/option[1]"),
        "Search": (By.XPATH, "(//div[contains(@class,'buttoncomponent')])[2]")
    }

    TEXT_OPTIONS = {
        "Languages": (By.XPATH, "//select[@name='Language']/option"),
        "Subjects": (By.XPATH, "//select[@name='Subject']/option"),
        "Grades": (By.XPATH, "//select[@name='Grade']/option")
    }
    IMAGE = {
        "Head_Text_FB": (By.XPATH, "//div[contains(@class,'bannercomponent')]/child::img"),
        "Container_Text_FB": (By.XPATH, "//img[@alt='Title']"),
        "Container_Image_FB": (By.XPATH, "//img[contains(@class,'imagecomponent')]")
    }
