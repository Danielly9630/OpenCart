from selenium.webdriver.common.by import By

class HomePage:
    #locators
    lnk_Register_xpath="//a[normalize-space()='Register']"
    lnk_Login_xpath="//a[normalize-space()='Log in']"


    #constructor
    def __init__(self, driver):
        self.driver=driver


    #action methods
    def click_Register(self):
        self.driver.find_element(By.XPATH,self.lnk_Register_xpath).click()

    def click_Login(self):
        self.driver.find_element(By.XPATH,self.lnk_Login_xpath).click()