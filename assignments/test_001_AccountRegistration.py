#import sys
#sys.path.append("../OpenCartProject/pageObjects")
from pageObjects.HomePageObjects import HomePage
from pageObjects.AccountRegistrationObjects import AccountRegistration



class Test_001_AccountRegistration:
    lnk_URL="https://demo.opencart.com/"
    
    def test_accountreg(self,setup):
        self.driver=setup
        
        self.driver.get(self.lnk_URL)
        self.driver.maximize_window()
        
        self.hp=HomePage(self.driver)
        self.hp.clickAccount()
        self.hp.clickRegister()
        self.regpage=AccountRegistration(self.driver)
        
        self.regpage.setFirstname("DanyDan")
        self.regpage.setLastname("Combi")
        self.regpage.setEmail("ahsjfivh@gmail.com")
        self.regpage.setPassword("sjhaifhj125")
        self.regpage.clickPolicy()
        self.regpage.clickContinue()
        self.confirmMsg=self.regpage.getConfirmationMsg()
        print(self.confirmMsg)
        self.driver.close()
        
        if self.confirmMsg=="Your Account Has Been Created!":
            assert True
        else:
            assert False
        
        
        
        
    