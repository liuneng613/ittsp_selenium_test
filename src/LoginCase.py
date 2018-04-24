from selenium.common.exceptions import NoSuchElementException

from browser_operation import Login
from sePublic import CustomizationLog
from sePublic import ReadConfig
from sePublic import ReadWriteExcelData

# Python导入模块的方法有两种：import module 和 from module import，区别是前者所有导入的东西使用时需加上模块名的限定，而后者不要。
my_logger = CustomizationLog.CustomizationLog("Login_Case")


class LoginCase:
    def __init__(self):
        self.test_excel = ReadWriteExcelData.ReadWriteExcelData(ReadConfig.root_path + r"\test_case\user_test.xlsx")
        self.test_list = self.test_excel.read_data('login')
        self.login_operation = Login.Login()

    @property
    def login_assertion(self):
        for i in range(1, len(self.test_list)):
            # 获取数据
            username = self.test_list[i][self.test_excel.col_index(self.test_list, 'username')]
            password = self.test_list[i][self.test_excel.col_index(self.test_list, 'password')]
            org_code = self.test_list[i][self.test_excel.col_index(self.test_list, 'org_code')]
            # TypeError: object of type 'NoneType' has no len() : None 与''不是一个东西
            if username is None:
                username = ''
            if password is None:
                password = ''
            if org_code is None:
                org_code = ''
            expected_results = self.test_list[i][self.test_excel.col_index(self.test_list, 'expected_results')]
            # 登陆操作
            self.login_operation.login(username, password, org_code)
            try:
                # 判断一个元素是否存在，返回一个bool值 operation_element_bool
                operation_element_bool = self.login_operation.dr.find_element_by_xpath(
                        '//*[@id="sy_user_notice_tool2"]').is_displayed()
                if operation_element_bool:
                    # 元素存在，给实际结果和测试结果赋值
                    self.test_list[i][self.test_excel.col_index(self.test_list, 'actual_results')] = \
                        self.login_operation.dr.find_element_by_xpath('//*[@id="sy_user_notice_tool2"]').text
                    self.test_list[i][self.test_excel.col_index(self.test_list, 'test_results')] = 'pass'
                    my_logger.info("用例[%s,%s,%s]通过！" % (username, password, org_code))
                    self.login_operation.dr.back()
                    self.login_operation.clear()
            except NoSuchElementException:
                actual_results = self.login_operation.dr.find_element_by_xpath(
                        '//*[@id="loginBody"]/div/div[1]/dv/div[2]/em').text
                # 预期结果与实现结果对比
                if expected_results == actual_results:
                    self.test_list[i][self.test_excel.col_index(self.test_list, 'actual_results')] = actual_results
                    self.test_list[i][self.test_excel.col_index(self.test_list, 'test_results')] = 'pass'
                    self.login_operation.clear()
                    my_logger.info("用例[%s,%s,%s]通过！" % (username, password, org_code))
                else:
                    self.test_list[i][self.test_excel.col_index(self.test_list, 'actual_results')] = actual_results
                    self.test_list[i][self.test_excel.col_index(self.test_list, 'test_results')] = 'fail'
                    # 失败时，保存图片到image目录
                    self.login_operation.dr.get_screenshot_as_file(
                            ReadConfig.root_path + r'\results\results_image\login_fail.png')
                    self.login_operation.clear()
                    my_logger.info("用例[%s,%s,%s]失败！" % (username, password, org_code))
        # 关闭浏览器
        self.login_operation.close_login()
        # 返回
        return self.test_list


if __name__ == '__main__':
    # login不是静态访求 ，不能通过类名直接调用 ，需要先创建一个类的对象
    test_user = LoginCase()
    s = test_user.login_assertion
    print(s)
    test_user.test_excel.write_data(s, 'login_case')
