from ui_test.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    post_loc = (By.ID,'post')
    submit_loc = (By.ID,'submit')

    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    sign_in_loc = (By.ID, 'submit')
    username = 'blues'
    password = '123456'

    def input_post(self,post):
        self.find_element(*self.post_loc).send_keys(post)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    def _open(self,url,page_title):
        self.driver.maximize_window()
        self.driver.get(url)
        self.find_element(*self.username_loc).send_keys(self.username)
        self.find_element(*self.password_loc).send_keys(self.password)
        self.find_element(*self.sign_in_loc).click()
