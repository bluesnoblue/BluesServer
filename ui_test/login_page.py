from ui_test.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    username_loc =  (By.ID, 'username')
    password_loc = (By.ID, 'password')
    remember_me_loc = (By.ID,'remember_me')
    sign_in_loc = (By.ID,'submit')
    register_loc = (By.ID,'register')
    reset_psw_loc = (By.ID,'reset_psw')

    def click_register(self):
        self.find_element(*self.register_loc).click()

    def click_reset_psw_loc(self):
        self.find_element(*self.reset_psw_loc).click()

    def click_sign_in(self):
        self.find_element(*self.sign_in_loc).click()

    def click_remember_me(self):
        self.find_element(*self.remember_me_loc).click()

    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

