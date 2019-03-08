import unittest
from ui_test.login_page import LoginPage
from selenium import webdriver

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = 'http://127.0.0.1:5000/'
        self.username = 'blues'
        self.password = '123456'

    def test_login(self):
        login_page = LoginPage(self.driver, self.url, 'Sign In - BluesServer')
        login_page.open()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.click_remember_me()
        login_page.click_sign_in()
        self.assertTrue(login_page.on_page('Home Page - BluesServer'))

    def test_skip_register(self):
        login_page = LoginPage(self.driver,self.url,'Sign In - BluesServer')
        login_page.open()
        login_page.click_register()
        self.assertTrue(login_page.on_page('Register - BluesServer'))

    def test_reset_psw(self):
        login_page = LoginPage(self.driver,self.url,'Sign In - BluesServer')
        login_page.open()
        login_page.click_reset_psw_loc()

    def tearDown(self):
        self.driver.quit()