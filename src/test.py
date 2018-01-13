
# cx_Oracle查询数据乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'



import cx_Oracle
conn1 = cx_Oracle.connect('c5web/c5web@192.168.3.138:1521/vms3devdb')
c = conn1.cursor()
# SELECT * FROM N_INSTRBACK WHERE VEHICLE_ROLL_CALL_ID = '-1531927313'
# select * from N_INSTRBACK
# SELECT VEHICLE_ID FROM V_VEHICLEINFO WHERE ID_NUMBER = '测A22332'
c.execute("UPDATE V_VEHICLEINFO SET MODEL_ID = '22' WHERE  ID_NUMBER  = '测A22332'")
conn1.commit()

# result = c.fetchall()
# print(result)
# print(x.fetchone()[0])

# print(x.fetchmany(5))

# print(x.fetchall())

conn1.close()
# driver = webdriver.Firefox()
# driver.get('https://www.baidu.com')
# driver.get_window_size(1024, 768)
# # driver.maximize_window()


# s = Login.Login()
# s.login('system', 'system@123', 'B')
# sleep(10)
#
# s.dr.find_element_by_xpath('//*[@id="statusFileDiv"]/label[2]').click()
#
# s.dr.find_element_by_xpath('//*[@id="_easyui_tree_59"]/span[2]').click()
# s.dr.find_element_by_xpath('//*[@id="_easyui_tree_60"]/span[3]').click()
# s.dr.find_element_by_xpath('//*[@id="_easyui_tree_64"]/span[4]').click()
# s.dr.find_element_by_xpath('//*[@id="_easyui_tree_21"]/span[7]').click()
#
# test01 = s.dr.find_element_by_xpath('//*[@id="_easyui_tree_21"]/span[8]/span[1]').text
#
# if test01 == '(停车)':
#     print('pass')
# else:
#     print(test01)

# s = Login.Login()
# s.login('system', 'system@123', 'B')
# bool_test = s.dr.find_element_by_xpath('//*[@id="sy_user_notice_too2"]').is_displayed()
# print(s.dr.find_element_by_xpath('//*[@id="sy_user_notice_tool2"]').text)
# print(bool_test)
#
# try:
#     a = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="mainlayout_body"]/div[1]/div/div[1]/font')))
#     if a.is_displayed():
#         print('pass')
#     else:
#         print('fail')
# except TimeoutException:
#     print('fail')

# wb = Workbook()
# print(wb.get_sheet_names())
# ws1 = wb.active
# ws1.title = "登录"
# print(wb.get_sheet_names())
# ws3 = wb.create_sheet(title="Data")
# print(wb.get_sheet_names())
# row = [1,2,3,4,5]
# ws1.append(row)
# wb.save(read_config.root_path + r'\results\login.xlsx')

# list1 = [['用例编号', '用户名', '密码', '组织编码', '预期结果', '实际结果', '测试结果'],
#          [1, 'system', 123, 'B', '登录信息验证失败', None, None],
#          [2, 'system123', 123, 'B', '登录信息验证失败', None, None],
#          [3, 'system', 'system@123', 'B00001', '登录信息验证失败', None, None],
#          [4, 'system', 'system@123', 'B', '成功', None, None]]
#
# print(len(list1))




