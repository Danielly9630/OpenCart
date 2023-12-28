from selenium.webdriver.common.by import By


class HomePage():
    #locators
    lnk_MyAccount_xpath="//span[normalize-space()='My Account']"
    lnk_Register_xpath="//a[normalize-space()='Register']"
    lnk_Login_xpath="//a[normalize-space()='Login']"

    #constructors
    def __init__(self, driver):
        self.driver=driver


    #action methods
    
    def clickAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_MyAccount_xpath).click()
        
    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_Register_xpath).click()
    
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.lnk_Login_xpath).click()