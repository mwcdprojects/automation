#!C:\Python27\python.exe

"""
Testcase :Search by Aadhaar
Expected Result: Bebeficiary search result should be displayed.

"""
import sys
import unittest
from selenium import webdriver
import time
import string
import random
import verhoeff



class login(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")


    def test_01_aadhaarno(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************ #
        # Search By Aadhaar Number #
        # ************************ #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("dataentry_testautomation@mailinator.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd1")
        print "Password entered"
        time.sleep(3)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title
        time.sleep(1)
        self.driver.find_element_by_link_text("Report").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Payments Report").click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//select[@id='Month']/option")[1].click()
        self.driver.find_elements_by_xpath("//select[@id='Year']/option")[1].click()
        self.driver.find_elements_by_xpath("//select[@id='Verifier']/option")[2].click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//select[@id='FieldFunctionary']/option")[2].click()
        self.driver.find_element_by_xpath("//input[@class='btn btn-primary']").click()
        print self.driver.find_element_by_xpath("//div[@class='col-md-12 col-xs-12']/div/h4").text
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='col-md-12 col-xs-12']/div/h4").text ,"Payment Report")

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