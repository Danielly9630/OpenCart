from pageObjects.HomePageClass import HomePage
from pageObjects.RegisterPageClass import RegisterDemo
from utilities.randomString import randomStringGenerator
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import os
import pytest


class TestAccountRegistration:
    baseURL = ReadConfig.getApplicationURL() #"https://demo.nopcommerce.com/"
    logger = logGen.loggen() #log generation

    @pytest.mark.regression
    def test_accountRegister(self,setup):
        self.logger.info("***** Test_001_AccountRegistration starting... ****")
        self.driver=setup


        self.driver.get(self.baseURL)
        self.logger.info("Launching Application.....")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.reg=RegisterDemo(self.driver)

        self.logger.info("Clicking on Register")
        self.hp.click_Register()

        self.logger.info("Proving the customer's registration info...")
        self.reg.clickFemaleGender()
        self.reg.setFirstname("Danie Minnie")
        self.reg.setLastname("Jaxkson")
        self.reg.setDate("15","October","2010")
        self.reg.setEmail("abvgf@gmail.com")
        #self.email=randomStringGenerator()+"@gmail.com"
        #print(self.email)
        #self.reg.setEmail(self.email)
        self.reg.setCompanyName("Jean Tabi")
        self.reg.setPwd(ReadConfig.getPassword()) #("KJHhsfd256")
        self.reg.setConfirmPwd(ReadConfig.getPassword())  #"KJHhsfd256")
        self.reg.clickRegister()
        self.ConfirMsg=self.reg.getConfMsg()
        
        if self.ConfirMsg=="Your registration completed":
            self.logger.info("Account registration is passed...")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/RegistrationFailed.png") # -----> this worked for RUN button
            #self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png") #does not work
            self.logger.error("Account registration is failed...")
            assert False
            self.driver.close()

        self.logger.info("***** Test_001_AccountRegistration finished... ****")

        
        
        
        
        