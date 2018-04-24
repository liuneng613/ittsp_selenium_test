# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://dev.woordee.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/login.html")
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("13554514655")
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("123456")
        driver.find_element_by_id("normLogin").click()
        driver.find_element_by_css_selector("div.boxFooter > p").click()
        driver.find_element_by_id("sourceLang").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.hover").click()

        driver.find_element_by_link_text(u"确定").click()
        time.sleep(2)
        driver.find_element_by_id("targetLang").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#LAY_layuipro_tar > div.tarLang > div.lang > #moreLang > li > a").click()
        time.sleep(2)

        driver.find_element_by_css_selector("#LAY_layuipro_tar > div.btnGroup > div.btnRight > button.btn.targetYesbtn").click()
        time.sleep(2)
        driver.find_element_by_id("contents").clear()
        driver.find_element_by_id("contents").send_keys("testliun")
        time.sleep(2)
        driver.find_element_by_link_text(u"确定").click()
        time.sleep(2)
        driver.find_element_by_css_selector("button.router_go.customerBtn").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
