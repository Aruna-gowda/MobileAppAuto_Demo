# import allure
# from TestCases.BaseTest import BaseTest
# from PageObjects.LoginPage import *

# class TestLoginPage(BaseTest):
#     global driver

#     @allure.title("Verify User able to login with valid Credentials")
#     def test_TC001_ValidCredentials(self):
#         LoginPage(self.driver).Login()
#     #
#     @allure.title("Verify User can't login with Invalid Credentials")
#     def test_TC002_InValidCredentials(self):
#         LoginPage(self.driver).InValid_Login()
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHomePage():

    @allure.title("Verify User able to login with valid Credentials")
    def test_TC002_ValidCredentials(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument( '--headless' )
        options.add_argument("--disable-notifications")
        options.add_argument( "--start-maximized" )
        options.add_experimental_option('excludeSwitches', ['enable-logging'] )
        driver = webdriver.Chrome(options=options)

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://stage-app.edifyai.com/login")
        driver.quit()
