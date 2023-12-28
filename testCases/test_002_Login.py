import pytest

from pageObjects.HomePageClass import HomePage
from pageObjects.LoginPageClass import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import pytest

class TestLogin:
    baseURL = ReadConfig.getApplicationURL()  # "https://demo.nopcommerce.com/"
    logger = logGen.loggen()  # log generation

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("****test_002_Login is started.........***")
        self.driver=setup

        self.logger.info("Launching the Application...")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #objects
        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)

        self.logger.info("Clicking on Login...")
        self.hp.click_Login()
        self.logger.info("Setting the customer's info")
        self.lp.setMyEmail(ReadConfig.getUseremail())
        self.lp.setMyPwd(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.ConfLogin=self.lp.isLogoutpresent()
        #print((self.ConfLogin))
        if self.ConfLogin=="Log out":
            self.logger.info("Login is passed...")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/LoginFailed.png")
            # self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png") #does not work
            self.logger.error("Login is failed...")
            assert False
            self.driver.close()

        self.logger.info("***** Test_002_Login finished... ****")
