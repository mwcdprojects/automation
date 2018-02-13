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
        password.send_keys("P@ssw0rd")
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
        # self.driver.switch_to_alert()
        time.sleep(2)
        # self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonpane ui-widget-content ui-helper-clearfix']/div/button[1]").click()
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
    def test_02_add_a_beneficiary(self):
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
        time.sleep(1)
        self.driver.find_element_by_id("btnNewbeneficiary").click()
        time.sleep(2)

        # Fill in all the valid details #
        """
        self.driver.find_element_by_id("dpicker1").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[5]").click()
        time.sleep(1)
        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(1)
        #print Aadhaar_avaialbilty_data[1].get_attribute('value')
        Aadhaar_avaialbilty_data[1].click()
        time.sleep(1)
        Aadhar_husband_availability = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        Aadhar_husband_availability[1].click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//select[@id='beneficiaryAltID']/option[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='fatherAltID']/option[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtAlternateNumber']").send_keys("test1234567")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='BenAlternateIdCheck']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='txtFatherAlternateNumber']").send_keys("testhusband1234567")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='HusbandAlternateIdCheck']").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblBenAlternateIdStatus']").text , "Id Proof Number is allowed for Registration")
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblHusbandAlternateIdStatus']").text, "Id Proof Number is allowed for Registration")
        self.driver.find_element_by_xpath("//input[@id='NameAsInIDCard']").send_keys("Reena")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='FNameAsInIDCard']").send_keys("Kumar")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='Phone']").send_keys("9987643293")
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Category']/option[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='dpicker2']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[1]/td[5]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='dpicker3']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[5]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='drpAnganvaadi']/option[4]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@id='AreaLocalitySector']").send_keys("Kerela")
        time.sleep(2)
        """
        # Find Bankdetails

        self.driver.find_element_by_xpath("//a[@id='ifscButton']").click()
        time.sleep(2)
        self.driver.switch_to_active_element()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='idOk']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='ifscButton']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='txtBank']/option[34]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='txtStateBank']/option[15]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtCity']").send_keys("Chennai")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtBranch']").send_keys("Chromepet")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='idCancel']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='txtBank']/option[34]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='txtStateBank']/option[15]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtCity']").send_keys("Chennai")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtBranch']").send_keys("Chrompet")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='idSearch']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//table[@class='table table-striped grid-table']/tbody/tr/td/input").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='ID']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='idOk']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='BankAccountNo']").send_keys("1234670334261123")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='txtAccountHoldersName']").send_keys("Reema")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='btnVerify']").click()
        time.sleep(5)
        self.driver.switch_to_active_element()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(5)
        self.driver.implicitly_wait(20)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/h5").text , " The beneficiary application form is sent for approval")


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
