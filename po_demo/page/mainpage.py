from telnetlib import EC
from time import sleep

import allure
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from po_demo.base.basepage import BasePage
from po_demo.page.book_title import BookTitle



class MainPage(BasePage):

    __login_button = (By.CLASS_NAME, "index_top_operation_loginBtn")
    __quit_button = (By.ID, "logout")
    __book_title = (By.XPATH, "//*[@id='menu_contacts']")




    def login(self):
        # 点击企业微信登陆按钮
        self.find(self.__login_button).click()
        with allure.step("获取本地cookies,并使用"):
            # 获取本地cookies
            with open("../cookie.yaml") as cookies:
                cookies = yaml.safe_load(cookies)
            for i in cookies:
                self.driver.add_cookie(i)

        # wait_action.until(expected_conditions.presence_of_element_located(self.__book_title))
        # logoutbutton = self.driver.find_element(By.ID, "logout")
        self.webwait(expected_conditions.visibility_of_element_located((By.ID, "logout")))
        cookie = self.driver.get_cookies()
        with open("../cookie.yaml", "w", encoding="utf-8") as cookie_file:
            yaml.safe_dump(cookie, cookie_file)

        return self

    #进入通讯录
    def title_book(self):
        self.find(self.__book_title).click()

        self.webwait(expected_conditions.presence_of_element_located((By.CLASS_NAME, "js_party_info")))
        return BookTitle(self.driver)


