import sys
import collections
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random




class login(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""

        self.driver = webdriver.Chrome("C:\\Users\\arche\\chromedriver_win32\\chromedriver.exe")


    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation123@mailinator.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print "Password entered"
        time.sleep(3)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='main-menu']/div/ul[3]/li/a").click()
        self.driver.find_element_by_link_text("Payments Report").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='Month']/option[1]").click()
        self.driver.find_element_by_xpath("//select[@id='Year']/option[2]").click()
        self.driver.find_element_by_xpath("//select[@id='Verifier']/option[2]").click()
        self.driver.find_element_by_xpath("//select[@id='FieldFunctionary']/option[2]").click()

        self.driver.find_elements_by_tag_name("input")[0].click()
        assert self.driver.find_element_by_xpath("//div[@class='col-md-12 col-xs-12 report_container report_outer_container']/h4").text == "Payment Report"
        print self.driver.find_element_by_xpath("//div[@class='col-md-12 col-xs-12 report_container report_outer_container']/h4").text
        print self.driver.find_element_by_xpath("//div[@class='col-md-12 col-xs-12 report_container report_outer_container']/h5").text



    def tearDown(self):
        if self.driver.title == "PRADHAN MANTRI MATRU VANDANA YOJANA":
            self.driver.quit()
        else:
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[@class='dropdown']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//a[@id='btnlogout']").click()
            time.sleep(1)
            self.assertIn("PRADHAN MANTRI MATRU VANDANA YOJANA", self.driver.title)
            print self.driver.title
            print "User Logged out Successfully"
            self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)