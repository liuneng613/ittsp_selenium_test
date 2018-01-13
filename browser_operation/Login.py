from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from public import CustomizationLog, readConfig

# Python导入模块的方法有两种：import module 和 from module import，区别是前者所有导入的东西使用时需加上模块名的限定，而后者不要。
my_logger = CustomizationLog.CustomizationLog("LoginCase")


class Login:
    """
    创建浏览器对象
    登陆
    清空文本框
    关闭浏览器
    """

    def __init__(self):
        # 创建浏览器对象
        self.dr = webdriver.Firefox()
        self.dr.get(readConfig.ittsp_url)
        self.dr.maximize_window()

    def login(self, username, password, org_code):
        # 用户登陆操作

        try:
            self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').send_keys(username)
            self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').send_keys(password)
            self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').send_keys(org_code)
            self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[5]/input').click()
        except NoSuchElementException as msg:
            my_logger.error("selenium.common.exceptions.NoSuchElementException:%s" % msg)

    def clear(self):
        # 清空username\password\org_code文本框
        self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').clear()

    def close_login(self):
        # 关闭浏览器
        self.dr.quit()


if __name__ == '__main__':
    test = Login()
    test.login('system', 'system@123', 'B')


