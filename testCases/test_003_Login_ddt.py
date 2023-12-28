import time
import pytest
from pageObjects.HomePageClass import HomePage
from pageObjects.LoginPageClass import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import ExcelUtils

class TestLoginDDT:
    baseURL = ReadConfig.getApplicationURL()  # "https://demo.nopcommerce.com/"
    logger = logGen.loggen()  # log generation
    file = "./testData/Login_ddt.xlsx"
    sheetname = "LoginDDT"

    @pytest.mark.first
    def test_loginddt(self,setup):
        self.logger.info("****test_003_Login_ddt is started.........***")
        self.logger.info("Counting rows from XL file...")
        self.Rows = ExcelUtils.getRowCount(self.file, self.sheetname)
        lst_status = []

        self.driver=setup
        self.logger.info("Launching the Application...")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #objects
        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)


        for r in range(2,self.Rows+1):
            self.logger.info("Clicking on Login...")
            self.hp.click_Login()
            self.logger.info("Reading data from XL file...")
            self.email = ExcelUtils.readData(self.file,self.sheetname,r,1)
            self.pwd = ExcelUtils.readData(self.file, self.sheetname, r, 2)
            self.exp_res = ExcelUtils.readData(self.file, self.sheetname, r, 3)
            self.logger.info("Setting the customer's info for Login")
            self.lp.setMyEmail(self.email)
            self.lp.setMyPwd(self.pwd)
            self.lp.clickLogin()
            time.sleep(2)
            #self.ConfLogin=self.lp.isLogoutpresent()
            self.Login_res=self.lp.isLoginNotOk()

            if self.exp_res=="Valid":
                if self.Login_res==False:
                    self.logger.info("Login_ddt is passed...")
                    lst_status.append("Pass")
                    self.lp.clickLogout()

                else:
                    self.logger.error("Login_ddt is failed...")
                    lst_status.append("Fail")

            elif self.exp_res=="Invalid":
                if self.Login_res==False:
                    self.logger.error("Login_ddt is failed...")
                    lst_status.append("Fail")
                    self.lp.clickLogout()
                else:
                    self.logger.info("Login_ddt is passed...")
                    lst_status.append("Pass")

        self.driver.close()


        #Final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False

        self.logger.info("***** Test_003_Login_ddt finished... ****")