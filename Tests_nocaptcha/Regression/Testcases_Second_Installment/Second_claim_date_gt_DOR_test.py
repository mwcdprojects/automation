#!C:\Python27\python.exe

"""
Testcase :Date of Second Claim > Date of Registration
Expected Result: Should accept the form

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

    def test_01(self):
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

        self.driver.find_element_by_id("btnNewbeneficiary").click()
        time.sleep(3)


    def test_02(self):
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

        self.driver.find_element_by_id("dpicker1").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[2]").click()
        time.sleep(1)
        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(1)
        # print Aadhaar_avaialbilty_data[1].get_attribute('value')
        Aadhaar_avaialbilty_data[1].click()
        time.sleep(1)
        Aadhar_husband_availability = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        Aadhar_husband_availability[1].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='beneficiaryAltID']/option[7]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtAlternateNumber']").send_keys("KN100000013")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='BenAlternateIdCheck']").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//label[@id='lblBenAlternateIdStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblBenAlternateIdStatus']").text,
                        "Id Proof Number is allowed for Registration")

        self.driver.find_element_by_xpath("//select[@id='fatherAltID']/option[7]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtFatherAlternateNumber']").send_keys("KN100000015")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='HusbandAlternateIdCheck']").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//label[@id='lblHusbandAlternateIdStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblHusbandAlternateIdStatus']").text,
                        "Id Proof Number is allowed for Registration")
        self.driver.find_element_by_xpath("//input[@id='NameAsInIDCard']").send_keys("Nilima")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='FNameAsInIDCard']").send_keys("Nadeem")
        time.sleep(1)

        self.driver.find_element_by_xpath("//input[@id='Phone']").send_keys("9990000016")
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Category']/option[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='HealthId']").send_keys('HID1110017')
        self.driver.find_element_by_xpath("//input[@id='dpicker2']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='dpicker3']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[6]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//input[@id='AddressLine1']").send_keys('110')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AddressLine2']").send_keys('2nd Main')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AddressLine3']").send_keys('Bull Temple Road')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AreaLocalitySector']").clear()
        self.driver.find_element_by_xpath("//input[@id='AreaLocalitySector']").send_keys('Alankady')
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='drpAnganvaadi']/option[4]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@id='Pincode']").send_keys('670645')
        time.sleep(1)
        self.driver.find_element_by_id("BankIFSCCode").send_keys("SBIN0005099")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='ifscButton1']").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//label[@id='lblStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblStatus']").text, "Valid IFSC Code")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='BankAccountNo']").send_keys("12345000017")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='txtAccountHoldersName']").send_keys("Nilima")
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
        print self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/h5").text
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/h5").text , " The beneficiary application form is sent for approval")
        installments = self.driver.find_elements_by_xpath("//div[@class='col-md-12']/a")
        installments[1].click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='dpicker']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[8]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='dpicker1']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[7]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[7]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='btnSave']").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        print self.driver.find_element_by_xpath("//div[@class='md-col-12']/p[2]").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='md-col-12']/p[2]").text , "Second Instalment Saved Successfully")


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