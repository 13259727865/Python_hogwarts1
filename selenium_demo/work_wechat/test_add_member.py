
from time import sleep

import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("添加企业成员测试")
class TestAddMwmber:


    def setup_class(self):
        #实例化driver
        self.driver = webdriver.Chrome()
        #实例化鼠标操作类
        self.actions = ActionChains(driver=self.driver)
        #访问企业微信连接
        self.driver.get("https://work.weixin.qq.com/")
        #设置全局5秒隐式等待
        self.driver.implicitly_wait(10)
        #点击企业微信登陆按钮
        self.driver.find_element(By.CLASS_NAME, "index_top_operation_loginBtn").click()
        with allure.step("获取本地cookies,并使用"):
            #获取本地cookies
            with open("cookie.yaml") as cookies:
                cookies = yaml.safe_load(cookies)
            for i in cookies:
                self.driver.add_cookie(i)

        #手动扫码并获取cookie存储
        self.wait_action = WebDriverWait(self.driver, 30)
        self.wait_action.until(EC.presence_of_element_located((By.ID, "logout")))
        cookie = self.driver.get_cookies()
        with open("cookie.yaml","w",encoding="utf-8") as cookie_file:
            yaml.safe_dump(cookie,cookie_file)

        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()





    def teardown_class(self):
        with allure.step("关闭浏览器"):
            self.driver.close()

    @allure.story("不填写必填字段测试")
    def test_add_nonename(self):
        with allure.step("进入添加页面"):
            self.driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>.js_add_member").click()
        with allure.step("进入页面后直接点击保存"):
            # self.wait_action.until(EC.visibility_of_element_located(self.driver.find_element(By.CLASS_NAME, "js_btn_save")))
            save_button=self.driver.find_element(By.CLASS_NAME, "js_btn_save")
            self.actions.click_and_hold(save_button).perform()
        with allure.step("获取提示并断言"):
            isplay_name=self.driver.find_element(By.XPATH,"//*[text()='请填写姓名']")
            pytest.assume(isplay_name.is_displayed())
        with allure.step("退出添加页面"):
            self.driver.find_element(By.CLASS_NAME, "js_btn_cancel").click()

    @allure.story("常规添加测试")
    def test_add_member(self):
        ele = self.driver.find_elements(By.XPATH,"//*[@id='member_list']/*")
        print("qian",len(ele))
        with allure.step("进入添加页面"):
            self.driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>.js_add_member").click()
        with allure.step("依次添加姓名、编号、手机后保存"):
            self.driver.find_element(By.ID,"username").send_keys("hanc")
            self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("012")
            self.driver.find_element(By.ID,"memberAdd_phone").send_keys("13259720012")
            self.driver.find_element(By.CLASS_NAME, "js_btn_save").click()
        sleep(3)
        ele1 = self.driver.find_elements(By.XPATH, "//*[@id='member_list']/*")
        print("hou",len(ele1))
        assert len(ele) + 1 ==len(ele1)


#js_contacts57 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member

