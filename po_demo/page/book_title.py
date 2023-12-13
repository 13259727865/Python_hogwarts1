
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po_demo.base.basepage import BasePage
from po_demo.page.add_member import AddMember

class BookTitle(BasePage):

    __add_button = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>.js_add_member")
    __TIPS_INFO = (By.CSS_SELECTOR, '.member_fixedTip_exportLink.js_export_unactived')
    __member_par = (By.XPATH, "//*[@id='member_list']/*")

    def add_member_button(self):
        with allure.step("进入添加页面"):
            self.find(self.__add_button).click()
        return AddMember(self.driver)

    #获取成员列表
    def get_member_list(self):

        self.webwait(expected_conditions.visibility_of_element_located(self.__TIPS_INFO))
        eles = self.finds(self.__member_par)

        return eles