from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AccountRegistration():
    #locators
    txt_firstname_id="input-firstname"
    txt_lastname_id="input-lastname"
    txt_email_id="input-email"
    txt_password_id="input-password"
    chk_policy_name="agree"
    btn_continue_xpath="//button[normalize-space()='Continue']"
    txt_msg_conf_xpath="//title[normalize-space()='Your Account Has Been Created!']"
    
    
    #constructors
    def __init__(self, driver):
        self.driver=driver
    
    
    #action methods
    def setFirstname(self,firstname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(firstname)
    
    def setLastname(self,lastname):
        self.driver.find_element(By.ID,self.txt_lastname_id).send_keys(lastname)
    
    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)
        
    def setPassword(self,firstname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(firstname)
        
    
    def clickPolicy(self):
        policyElement=self.driver.find_element(By.NAME,self.chk_policy_name)
        policyElement.send_keys(Keys.SPACE)  # for checkbox etc

        #wait = WebDriverWait(self.driver, 30)
        #ActionChains(self.driver).move_to_element(
            #wait.until(EC.element_to_be_clickable((By.NAME,self.chk_policy_name)))).click().perform()

        #self.driver.execute_script("arguments[0].scrollIntoView();", policyElement)
        #policyElement.click()

    
    def clickContinue(self):
        continue_Btn=self.driver.find_element(By.XPATH,self.btn_continue_xpath)
        #continue_Btn.send_keys("\n")  #send enter for links, buttons
        self.driver.execute_script("arguments[0].scrollIntoView();", continue_Btn)
        self.driver.execute_script("arguments[0].click();", continue_Btn)

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_msg_conf_xpath).text
        except:
            None
        
        