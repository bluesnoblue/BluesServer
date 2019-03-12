import unittest
from ui_test.home_page import HomePage
from selenium import webdriver
import time
class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = 'http://127.0.0.1:5000/'
        self.username = 'blues'
        self.password = '123456'

    def test_submit_post(self):
        home_page = HomePage(self.driver, self.url, 'Sign In - BluesServer')
        home_page.open()
        test_text = 'test_text%s'%str(time.time())
        home_page.input_post(test_text)
        home_page.click_submit()
        self.assertTrue(test_text in home_page.get_all_posts_text())

    def test_click_home(self):
        home_page = HomePage(self.driver, self.url, 'Sign In - BluesServer')
        home_page.open()
        home_page.click_home()
        self.assertTrue(home_page.on_page('Home Page - BluesServer'))

    def test_click_explore(self):
        home_page = HomePage(self.driver, self.url, 'Sign In - BluesServer')
        home_page.open()
        home_page.click_explore()
        self.assertTrue(home_page.on_page('Explore - BluesServer'))

    def test_click_profile(self):
        home_page = HomePage(self.driver, self.url, 'Sign In - BluesServer')
        home_page.open()
        home_page.click_profile()
        self.assertTrue(home_page.on_page('Profile - BluesServer'))

    def test_logout(self):
        home_page = HomePage(self.driver, self.url, 'Sign In - BluesServer')
        home_page.open()
        home_page.click_logout()
        self.assertTrue(home_page.on_page('Sign In - BluesServer'))

    def tearDown(self):
        self.driver.quit()
