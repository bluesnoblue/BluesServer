from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,base_url,page_title):
        self.driver = webdriver.Firefox()
        self.base_url = base_url
        self.page_title = page_title

    def on_page(self,page_title):
        return page_title in self.driver.title

    def _open(self, url,page_title):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(page_title), '页面打开失败%s'%url

    def open(self):
        self._open(self.base_url,self.page_title)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            print('%s页面中未能找到%s元素' % (self, loc))
            print(e)

    def swich_frame(self):
        pass

    def script(self,src):
        self.driver.execute_script(src)













