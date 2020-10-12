from selenium import webdriver
from selenium.webdriver.common.by import By

from lib.reporter import Reporter
from lib.selenium_extensions import (Click, findElementBy, isDisplayed,
                                     isEnabled, isSelected, sendKeys,
                                     waitUntilDisplay, waitUntilExistInDOM,
                                     waitUntilHidden,select,multi_select)


class LoginPage:
    
    
    driver = None

    def __init__(self,driver):
        self.driver = driver
    
    userName = (By.ID, 'user_email')
    password = (By.ID,'user_password')
    loginError = (By.XPATH,'//div[contains(@class,"flash-msg error")]')
    submitButton = (By.XPATH,'//button[@type="submit"]')
    lstCountriesLocator = (By.XPATH,'//button[@type="submit"]')


    userNameElement=None
    pwordElement=None
    submitBttn=None
    lstCountries=None
   

   # Example to explain how to use the select method

    def select_country(self, strCountry):              
        # userNameElement = self.driver.find_element(*LoginPage.userName)
        lstCountries = self.driver.findElementBy(*LoginPage.lstCountriesLocator)
        lstCountries.select(strCountry)
        
   
    def set_userName(self, _userName):              
        # userNameElement = self.driver.find_element(*LoginPage.userName)
        userNameElement = self.driver.findElementBy(*LoginPage.userName)
        userNameElement.send_keys(_userName)
        
    
    
    def login_error_displayed(self):
        notifcationElement = self.driver.findElementBy(*LoginPage.loginError)
        
        if notifcationElement.waitUntilDisplay(3):
            Reporter.failed("Login Failed for error : {0}".format(notifcationElement.text))
            return False
        elif notifcationElement.waitUntilHidden(3):
            Reporter.passed("Login passed")
            return True
    
    
    def set_password(self, _password):
        pwordElement = self.driver.findElementBy(*LoginPage.password)        
        pwordElement.send_keys(_password)        
        
        
    def click_submit(self):
        submitBttn = self.driver.findElementBy(*LoginPage.submitButton)               
        submitBttn.click()
        
        
    def login(self,tdr=dict()):
        if waitUntilDisplay(userNameElement,30):            
            self.set_userName(tdr["userID"])
            self.set_password(tdr["Password"])        
            self.click_submit()
