#!C:\Python27\python.exe

"""
Testcase :Beneficiary form will get approved and will be sent for UIDAI verification
 if Aadhaar is provided and then to the PFMS verification (bank details)

"""
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
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")


    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("block_panamaram@mailinator.com")
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
        time.sleep(3)

        # Beneficiary Approval

        self.driver.find_element_by_partial_link_text("INSTALMENT APPROVAL").click()
        time.sleep(2)
        #print self.driver.find_element_by_partial_link_text("BENEFICIARY APPROVAL")
        #print self.driver.find_element_by_xpath("//div[@class='tab-content']")
        #print self.driver.find_element_by_id("Beneficiary")
        frame = self.driver.find_element_by_xpath("//iframe[@id='approvalQueueGrid1']")
        self.driver.switch_to_frame(frame)
        self.driver.find_elements_by_xpath("//span[@class='grid-filter-btn']")[1].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("Diya")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='btn btn-info approve-btns']").click()
        self.driver.switch_to_active_element()
        time.sleep(1)
        buttons = self.driver.find_elements_by_xpath("//div[@class='ui-dialog-buttonset']/button")
        print len(buttons)
        for each in buttons:
            print each.text
        buttons[1].click()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)

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