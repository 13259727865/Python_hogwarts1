import allure
from selenium.webdriver.common.by import By

from po_demo.base.basepage import BasePage



class AddMember(BasePage):

    def add_member(self,username,acctid,phone):
        with allure.step("依次添加姓名、编号、手机后保存"):
            self.driver.find_element(By.ID, "username").send_keys(username)
            self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(acctid)
            self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
            self.driver.find_element(By.CLASS_NAME, "js_btn_save").click()
            from po_demo.page.book_title import BookTitle
        from po_demo.page.mainpage import MainPage
        return BookTitle(self.driver)