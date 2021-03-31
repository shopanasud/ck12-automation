from selenium.webdriver.common.by import By


class StaticFooterLocators(object):

    LINK_OVERVIEW = (By.XPATH, "// a[@id='footer_overview']")
    LINK_EMAIL = (By.XPATH, "//a[@id='footer_email']")
    MODAL_OVERVIEW = (By.XPATH, "//div[@id='myModal']")
    MODAL_EMAIL = (By.XPATH, "//div[@id='shareViaEmailModal']")
    MODAL_OVERVIEW_HEADING = (By.CSS_SELECTOR, "div[id='myModal'] h4")
    MODAL_EMAIL_HEADING = (By.XPATH, "//span[@class='share-context']")
    TEXT_OVERVIEW = "CK-12 Overview"
    TEXT_EMAIL = "Share CK-12 Foundation"
    MODAL_OVERVIEW_CLOSE = (
        By.XPATH, "//div[@class='close close-reveal-modal button-close']")
    MODAL_EMAIL_CLOSE = (By.XPATH, "//a[normalize-space()='+']")

    footer_links = {

        "xpath,//a[@id='footer_mission']": "Mission | CK-12 Foundation",
        "xpath,//a[@id='footer_team']": "Team | CK-12 Foundation",
        "xpath,//a[@id='footer_partners']": "Partners | CK-12 Foundation",
        "xpath,//a[@id='footer_pres']": "Press | CK-12 Foundation",
        "xpath,//a[@id='footer_careers']": "Passionate about education?So are we. | CK-12 Foundation",
        "xpath,//a[@id='footer_security']": "Security at CK-12 Foundation | CK-12 Foundation",
        "xpath,//a[@id='footer_status']": "CK-12 Foundation Status",
        "xpath,//a[@id='footer_success']": "Success Stories | CK-12 Foundation",
        "xpath,//a[@id='footer_blog']": "CK-12 Blog | General information about CK-12",
        "xpath,//a[@id='footer_usage_map']": "CK-12 Usage Map | CK-12 Foundation",
        "xpath,//a[@id='footer_testimonials']": "CK-12 Testimonials | CK-12 Foundation",
        "xpath,//a[@id='footer_jumpstart']": "Certified Educator Program | CK-12 Foundation",
        "xpath,//a[@id='footer_webinars']": "Webinars | CK-12 Foundation",
        "xpath,//a[@id='footer_implementation']": "Overview | CK-12 Foundation",
        "xpath,//a[@id='footer_pilot']": "Pilot Program | CK-12 Foundation",
        "xpath,//a[@id='footer_help']": "Help Center",
        "xpath,//a[@id='footer_contact']": "Contact Us | CK-12 Foundation",
        "xpath,//a[@id='footer_ccss']": "K-12 FlexBooks® | CK-12 Foundation",
        "xpath,//a[@id='footer_flexbooks']": "FlexBooks® | CK-12 Foundation",
        "xpath,//a[@id='footer_colege_flexbooks']": "K-12 FlexBooks® & Concepts | CK-12 Foundation",
        "xpath,//a[@id='footer_tools']": "Tools and Apps | CK-12 Foundation",
        "xpath,//a[@id='footer_braingenie']": "Braingenie",
        "xpath,//a[@id='footer_tou']": "Terms of Use | CK-12 Foundation",
        "xpath,//a[@id='footer_privacy']": "Privacy Policy | CK-12 Foundation",
        "xpath,//a[@id='footer_guidelines']": "Attribution Guidelines",
        "xpath,//a[@id='footer_facebook']": "CK-12 Foundation - Home | Facebook",
        "xpath,//a[@id='footer_twitter']": "CK-12 Foundation (@CK12Foundation) / Twitter",
        "xpath,//a[@id='footer_pinterest']": "CK-12 Foundation (ck12foundation) - Profile | Pinterest",
        "xpath,//a[@id='footer_linkedin']": "Sign Up | LinkedIn"

    }
