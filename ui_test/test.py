from selenium import webdriver
# from ui_test.login_page import LoginPage
from ui_test.home_page import HomePage
from selenium.webdriver.common.by import By

dr = webdriver.Firefox()
login_page = HomePage(dr, 'http://127.0.0.1:5000/', 'Sign In - BluesServer')
login_page.open()
print(login_page.get_all_posts_text())
# posts = dr.find_elements_by_xpath(xpath)
# for post in posts:
#     print(post.text)