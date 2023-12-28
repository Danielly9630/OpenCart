from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegisterDemo:
    #locators
    checkbox_male_id="gender-male"
    checkbox_female_id="gender-female"
    txtbox_firstname_id="FirstName"
    txtbox_lastname_id="LastName"
    select_days_xpath="//select[@name='DateOfBirthDay']"
    select_months_xpath="//select[@name='DateOfBirthMonth']"
    select_years_xpath="//select[@name='DateOfBirthYear']"
    txtbox_email_id="Email"
    txtbox_company_id="Company"
    txtbox_pwd_id="Password"
    txtbox_confirmpwd_id="ConfirmPassword"
    click_register_id="register-button"
    text_confmsg_xpath="//div[@class='result']"
    
    
    #constructors
    def __init__(self, driver):
        self.driver=driver
    
    
    #action methods
    def clickMaleGender(self):
        self.driver.find_element(By.ID,self.checkbox_male_id).click()
    
    def clickFemaleGender(self):
        self.driver.find_element(By.ID, self.checkbox_female_id).click()
    
    def setFirstname(self, firstname):
        self.driver.find_element(By.ID, self.txtbox_firstname_id).send_keys(firstname)
    
    def setLastname(self, lastname):
        self.driver.find_element(By.ID, self.txtbox_lastname_id).send_keys(lastname)
    
    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)
    
    def setCompanyName(self, company):
        self.driver.find_element(By.ID, self.txtbox_company_id).send_keys(company)
    
    def setPwd(self, pwd):
        self.driver.find_element(By.ID, self.txtbox_pwd_id).send_keys(pwd)
    
    def setConfirmPwd(self, confpwd):
        self.driver.find_element(By.ID, self.txtbox_confirmpwd_id).send_keys(confpwd)
    
    def clickRegister(self):
        self.driver.find_element(By.ID, self.click_register_id).click()
    
    def getConfMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_confmsg_xpath).text
        except:
            None
    
    def setDate(self,day,month,year):
        #setting the day
        Days=Select(self.driver.find_element(By.XPATH,self.select_days_xpath))
        Days.select_by_visible_text(day)
        
        #setting the month
        Months=Select(self.driver.find_element(By.XPATH,self.select_months_xpath))
        Months.select_by_visible_text(month)
        
        #setting the year
        Years=Select(self.driver.find_element(By.XPATH,self.select_years_xpath))
        Years.select_by_visible_text(year)
        