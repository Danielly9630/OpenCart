from selenium.webdriver.common.by import By

class LoginPage:
    #locators
    txt_email_id="Email"
    txt_pwd_id="Password"
    button_register_xpath="//button[normalize-space()='Register']"
    chk_rememberMe_id="RememberMe"
    lnk_forgotPwd_xpath="//a[normalize-space()='Forgot password?']"
    button_login_xpath="//button[normalize-space()='Log in']"
    lnk_logout_xpath="//a[normalize-space()='Log out']"
    text_ErrorMesLoginFailed_xpath="//div[@class='message-error validation-summary-errors']"


    #constructor
    def __init__(self,driver):
        self.driver=driver


    #action methods

    def setMyEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setMyPwd(self, pwd):
        self.driver.find_element(By.ID, self.txt_pwd_id).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def isLogoutpresent(self):
        try:
            return self.driver.find_element(By.XPATH, self.lnk_logout_xpath).text
        except:
            return False

    def isLoginNotOk(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_ErrorMesLoginFailed_xpath).is_displayed()
        except:
            return False
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()

