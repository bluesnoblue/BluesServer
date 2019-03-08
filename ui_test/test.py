from selenium import webdriver
# from ui_test.login_page import LoginPage
from ui_test.home_page import HomePage

dr = webdriver.Firefox()

login_page = HomePage(dr, 'http://127.0.0.1:5000/', 'Sign In - BluesServer')
login_page.open()
print(login_page.on_page('Home Page - BluesServer'))