#!C:\Python27\python.exe

"""
Testcases :
"""
import sys
import collections
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random




class login(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def _01_login(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://www.worldtimebuddy.com/")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        self.driver.find_element_by_id('tab_signin').click()
        # driver.find_element_by_xpath('//*[@id="tabs-func"]/li[1]/div/a[3]').click()
        self.driver.find_element_by_link_text("Email / Password").click()
        time.sleep(4)
        # wait = WebDriverWait(driver, 20)
        ##Enter email
        self.driver.find_element_by_name('email').click()
        self.driver.find_element_by_name('email').send_keys('rarthee@gmail.com')

        ##Enter password
        self.driver.find_element_by_name('password').click()
        self.driver.find_element_by_name('password').send_keys('sahana')

        ##Click submit

        self.driver.find_element_by_name('submit').click()
        # wait = WebDriverWait(driver, 10)
        time.sleep(4)
        # assert "Contentional Login - World Time Buddy" in driver.title
        assert self.driver.title == 'Time Converter and World Clock - Conversion at a Glance - Pick best time to schedule conference calls, webinars, online meetings and phone calls.'
        self.driver.quit()



    def test_02_addcountry(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://www.worldtimebuddy.com/")
        time.sleep(3)

        # **************** #
        # Add country #
        # **************** #
        location_list = self.driver.find_element_by_id("location_list")
        country = self.driver.find_element_by_id("location").send_keys("United States, California, San Jose")
        # list = self.driver.find_elements_by_id("location")
        # for i in list:
        #     text = i.get_attribute('onclick')
        #
        # self.driver.find_element_by_id("location_list")
        # self.driver.find_element_by_id("location").click()
        # Keys.ENTER
        # Keys.ARROW_DOWN
        timelist = self.driver.find_elements_by_class_name("hourline")
        ActionChains(self.driver).double_click()
        Keys.ENTER
        Keys.TAB
        self.driver.switch_to_active_element()
        self.driver.find_element_by_id("location").click()
        ActionChains(self.driver).perform()

    def test_03_addcountry(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://www.worldtimebuddy.com/")
        time.sleep(3)



    # def tearDown(self):
    #     self.driver.find_element_by_id("tab_account").click()
    #     time.sleep(1)
    #     if self.driver.find_element_by_link_text("Logout"):
    #         self.driver.find_element_by_link_text("Logout").click()
    #         self.driver.quit()
    #     else:
    #         self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)