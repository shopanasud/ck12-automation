from selenium.webdriver.common.by import By

class SigninLocators(object):
    #Class for SignIn Modal popup locators
    SIGNIN_WINDOW = (By.ID,"sign-in-modal")
    USER_NAME_FIELD = (By.XPATH,"//input[@name='login']")
    PASSWORD_FIELD = (By.XPATH,"//input[@name='token']")
    SIGNIN_BUTTON = (By.XPATH,"//body/div[@id='sign-in-modal']/div[1]/div[3]/div[1]/div[1]/div[1]/input[4]")

    # Signin through Google account
    SIGN_GOOGLE_BOTTON = (By.XPATH,"//span[contains(text(),'Sign in with Google')]")

    # Signin through facebook
    SIGNIN_FB_BUTTON = (By.XPATH,"//span[contains(text(),'Sign in with Facebook')]")
    #Facebook login page
    EMAIL_FIELD = (By.XPATH,"//input[@id='email']")
    FB_PASSWORD_FIELD = (By.XPATH,"//input[@id='pass']")
    FB_LOGIN_BUTTON = (By.XPATH,"//input[@name='login']")

    # Show more link
    SHOW_MORE_LINK = (By.XPATH,"//div[@id='show-more']")

    # SignIn through Twitter
    SIGNIN_TWITTER_BUTTON = (By.XPATH,"//span[contains(text(),'Twitter')]")
    #Twitter Login page
    TWITTTER_USERNAME_FIELD = (By.XPATH,"//input[@id='username_or_email']")
    TWITTER_PASSWORD_FIELD = (By.XPATH,"//input[@id='password']")
    TWITTER_AUTHORIZE_BUTTON = (By.XPATH,"//input[@id='allow']")

    #Signin through Microsoft
    SIGNIN_MICROSOFT_BUTTON = (By.XPATH,"//span[contains(text(),'Microsoft')]")

    # Forget password
    FORGET_PASSWORD_LINK = (By.LINK_TEXT,"Forgot Your Password?")

    # Signup if you dont have account in signin modal
    SIGNUP_ACCOUNT = (By.XPATH,"//a[contains(text(),'Sign up')]")


