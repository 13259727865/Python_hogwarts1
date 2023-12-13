from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from po_demo.util.logging import LogRoot


class BasePage:

    def __init__(self, exist_driver: WebDriver = None):
        if exist_driver == None:
            self.driver = webdriver.Chrome()
            # 访问企业微信连接
            self.driver.get("https://work.weixin.qq.com/")
            # 设置全局10秒隐式等待
            self.driver.implicitly_wait(10)
        else:
            self.driver = exist_driver

    def exit(self):
        self.driver.close()

    def find(self,args,optional=None):
        try:
            if optional == None:
                ele = self.driver.find_element(*args)
            else:
                ele = self.driver.find_element(args,optional)
        except Exception as e:
            ele = None
            LogRoot.error(f"参数有误或没找到元素:{e}")
        return ele

    def finds(self,args,optional=None):
        try:
            if optional == None:
                eles = self.driver.find_elements(*args)
            else:
                eles = self.driver.find_elements(args,optional)
        except Exception as e:
            eles = None
            LogRoot.error(f"参数有误或没找到元素:{e}")
        return eles

    def webwait(self,timeout=20,fun=None):
        wait_action = WebDriverWait(self.driver, timeout=timeout)
        ele = wait_action.until(fun())
        return ele

