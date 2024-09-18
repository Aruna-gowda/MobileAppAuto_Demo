import allure
from TestCases.BaseTest import BaseTest
from PageObjects.LoginPage import *

class TestLoginPage(BaseTest):
    global driver

    @allure.title("Verify User able to login with valid Credentials")
    def test_TC001_ValidCredentials(self):
        LoginPage(self.driver).Login()
    #
    @allure.title("Verify User can't login with Invalid Credentials")
    def test_TC002_InValidCredentials(self):
        LoginPage(self.driver).InValid_Login()