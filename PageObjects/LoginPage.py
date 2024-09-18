import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage
from Utilities import ReadConfigurations

platformName = ReadConfigurations.read_configuration("basic info","platformName")
if platformName == "Android":
    from Locators.Android import *
else:
    from Locators.iOS import *

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("Login into the mojo.ai application")
    def Login(self):
        Email = ReadConfigurations.read_configuration("basic info", "Email")
        Password = ReadConfigurations.read_configuration("basic info", "Password")
        self.Type(Email, "Input_Email_XPATH", Login.Input_Email_XPATH)
        self.Type(Password, "Input_Password_XPATH",Login.Input_Password_XPATH)
        self.Click("Button_Login_XPATH", Login.Button_Login_XPATH)
        self.Click("Button_Cancel_XPATH", Login.Button_Cancel_XPATH)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.XPATH, Home.Verify_Welcome_XPATH)))
        # self.check_display_status_of_element("Verify_Welcome_XPATH",Home.Verify_Welcome_XPATH)

    @allure.step("Login into the Mojo.ai application")
    def InValid_Login(self):
        self.Type("xyz@test.com", "Input_Email_XPATH", Login.Input_Email_XPATH)
        self.Type("abc@123", "Input_Password_XPATH", Login.Input_Password_XPATH)
        self.Click("Button_Login_XPATH", Login.Button_Login_XPATH)
        self.check_display_status_of_element("Verify_InvalidLogin_XPATH",Login.Verify_InvalidLogin_XPATH)
