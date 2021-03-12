from selenium.webdriver.common.by import By

class StaticFooterLocators(object):
    
    MODAL_OVERVIEW = (By.XPATH,"//div[@id='myModal']")
    MODAL_EMAIL = (By.XPATH, "//div[@id='shareViaEmailModal']")
    MODAL_HEADING =(By.CSS_SELECTOR, "div[id='myModal'] h4")
    MODAL_CLOSE = (By.XPATH,"//div[@class='close close-reveal-modal button-close']")
    MODAL_EMAIL_CLOSe = (By.XPATH, "//a[normalize-space()='+']")
    
    footer_links = {
        "xpath,//a[@id='footer_overview']" : "CK-12 Overview",
        "xpath,//*[@id='footer_mission']" : "Mission | CK-12 Foundation",
        "xpath,//span[.='Meet the Team']" : "Team | CK-12 Foundation",
        "xpath,//span[@data-i18n='c.f.partners']" : "Partners | CK-12 Foundation", 
        "xpath,//span[.='Press']" : "Press | CK-12 Foundation",
        "xpath,//span[.='Careers']" : "Passionate about education?So are we. | CK-12 Foundation",
        "xpath,//span[.='Security']" : "Security at CK-12 Foundation | CK-12 Foundation",
        "xpath,//span[.='Status']" : "CK-12 Foundation Status",
        "xpath,//span[.='Success Stories']" : "Success Stories | CK-12 Foundation",
        "xpath,//span[.='Blog']" : "CK-12 Blog | General information about CK-12",
        "xpath,//span[normalize-space()='CK-12 Usage Map']" : "CK-12 Usage Map | CK-12 Foundation",
        "xpath,//span[.='Testimonials']" : "CK-12 Testimonials | CK-12 Foundation",
        "xpath,//span[.='Certified Educator Program']" : "Certified Educator Program | CK-12 Foundation",
        "xpath,//span[.='Webinars']" : "Webinars | CK-12 Foundation",
        "xpath,//span[.='CK-12 Resources']" : "Overview | CK-12 Foundation",
        "xpath,//span[.='Pilot Program']" : "Pilot Program | CK-12 Foundation",
        "xpath,//span[.='Help']" : "Help Center",
        "xpath,//span[.='Contact Us']" : "Contact Us | CK-12 Foundation",
        "xpath,//a[@id='footer_ccss']" : "K-12 FlexBooks® | CK-12 Foundation",
        "xpath,//a[@id='footer_flexbooks']" : "FlexBooks® | CK-12 Foundation",
        "xpath,//a[@id='footer_colege_flexbooks']" : "K-12 FlexBooks® & Concepts | CK-12 Foundation",
        "xpath,//span[normalize-space()='Tools and Apps']" : "Tools and Apps | CK-12 Foundation",
        "xpath,//span[.='College FlexBooks®']" : "K-12 FlexBooks® & Concepts | CK-12 Foundation",
        "xpath,//a[.='BRAINGENIE™']" : "Braingenie",
        "xpath,//a[normalize-space()='Terms of Use']" : "Terms of Use | CK-12 Foundation",
        "xpath,//a[normalize-space()='Privacy']" : "Privacy Policy | CK-12 Foundation",
        "xpath,//a[normalize-space()='Attribution Guide']" : "Attribution Guidelines",
        "xpath,//a[@id='footer_facebook']" : "CK-12 Foundation - Home | Facebook",
        "xpath,//a[@id='footer_twitter']" : "CK-12 Foundation (@CK12Foundation) / Twitter",
        "xpath,//a[@id='footer_linkedin']" : "CK-12 Foundation | LinkedIn",
        "xpath,//a[@id='footer_pinterest']" : "CK-12 Foundation (ck12foundation) - Profile | Pinterest"
           
    }
    
    