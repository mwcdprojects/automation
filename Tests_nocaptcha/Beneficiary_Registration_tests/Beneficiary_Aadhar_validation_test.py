#!C:\Python27\python.exe
import sys
import collections
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""

    """
    def test_01_Register_Beneficiary(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
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

        # *************************************************** #
        # Register a Beneficiary with no field values entered #
        # Print the field validation errors ***************** #
        # *************************************************** #

        self.driver.find_element_by_id("btnNewbeneficiary").click()
        time.sleep(3)
        self.driver.find_element_by_id("btnVerify").click()
        #self.driver.switch_to_alert()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonpane ui-widget-content ui-helper-clearfix']/div/button[1]").click()
        self.driver.switch_to_active_element()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[2]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnVerify").click()
        self.driver.switch_to_active_element()
        self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        errors = self.driver.find_elements_by_xpath("//span[@class='field-validation-error']")
        for each in errors:
            print each.text
    """
    def test_02_Register_Beneficiary_Aadhaar_Number_check(self):

        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
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

        # ********************************************************* #
        # Register a Beneficiary and check for valid Aadhaar number #
        # ********************************************************* #

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("New Beneficiary").click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAadhar").send_keys("12341234")
        self.driver.find_element_by_id("BenAadhaarCheck").click()
        self.assertIn(self.driver.find_element_by_id("spnAadhar").text , 'The entered Aadhaar Number is invalid. Please enter again')
        time.sleep(1)
        self.driver.find_element_by_id("txtAadhar").clear()
        self.driver.find_element_by_id("txtAadhar").send_keys("472320554838")
        time.sleep(1)
        self.driver.find_element_by_id("BenAadhaarCheck").click()
        self.driver.switch_to_active_element()
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-buttons ui-draggable ui-resizable']").is_displayed())
        time.sleep(1)

        # Close the dialog box

        self.driver.find_element_by_xpath("//button[@class='ui-dialog-titlebar-close']").click()

        # Repeat the aadhar check and click Register a new beneficiary in the dialog box.

        self.driver.find_element_by_id("txtAadhar").clear()
        self.driver.find_element_by_id("txtAadhar").send_keys("472320554838")
        time.sleep(1)
        self.driver.find_element_by_id("BenAadhaarCheck").click()
        self.driver.switch_to_active_element()
        self.assertTrue(self.driver.find_element_by_xpath(
            "//div[@class='ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-buttons ui-draggable ui-resizable']").is_displayed())
        time.sleep(1)
        self.driver.find_element_by_id("btnNewRegistration").click()
        time.sleep(1)

        # Check for Aadhar validation for husband.

        self.driver.find_element_by_xpath("//input[@id='txtFAadhar']").send_keys("897953422753")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='HusbandAadhaarCheck']").click()
        time.sleep(1)
        self.driver.switch_to_active_element()
        self.assertTrue(self.driver.find_element_by_xpath(
            "//div[@class='ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-buttons ui-draggable ui-resizable']").is_displayed())
        time.sleep(1)

        # Close the dialog box

        self.driver.find_element_by_xpath("//button[@class='ui-dialog-titlebar-close']").click()


    def tearDown(self):
        if self.driver.title == "PRADHAN MANTRI MATRU VANDANA YOJANA":
            self.driver.quit()
        else:
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id=\"main-menu\"]/div/ul[5]/li/a").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("/html/body/nav[2]/div/div/div/ul[5]/li/ul/li[2]/a").click()
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
