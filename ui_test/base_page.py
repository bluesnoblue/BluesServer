from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):

    home_loc = (By.ID,'home')
    explore_loc = (By.ID, 'explore')
    profile_loc = (By.ID,'profile')
    logout_loc = (By.ID,'logout')
    login_loc = (By.ID,'login')

    def __init__(self,selenium_driver,base_url,page_title):
        self.driver = selenium_driver
        self.base_url = base_url
        self.page_title = page_title

    def on_page(self,page_title):
        return page_title in self.driver.title

    def _open(self,url,page_title):
        self.driver.maximize_window()
        self.driver.get(url)
        # assert self.on_page(page_title), u'打开页面失败%s' % url

    def open(self):
        self._open(self.base_url,self.page_title)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            print(e)
            print('%s页面中无法找到%s元素'%(self,loc))

    def find_elements(self,*loc):
        # try:
        WebDriverWait(self.driver,100).until(EC.visibility_of_all_elements_located(loc))
        return self.driver.find_elements(*loc)
        # except Exception as e:
        #     print(e)
        #     print('%s页面中无法找到%s元素'%(self,loc))


    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self,loc,vaule,clear_first=True,click_first=True):
        try:
            loc = getattr(self,'_%s'% loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print('%s页面中无法找到%s元素' % (self, loc))

    def click_home(self):
        self.find_element(*self.home_loc).click()

    def click_explore(self):
        self.find_element(*self.explore_loc).click()

    def click_profile(self):
        self.find_element(*self.profile_loc).click()

    def click_login(self):
        self.find_element(*self.login_loc).click()

    def click_logout(self):
        self.find_element(*self.logout_loc).click()