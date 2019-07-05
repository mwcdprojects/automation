#!C:\Python27\python.exe

"""
Testcase :Adhaar Number provided for both Beneficiary and Husband
Expected Result: Eligible for first installment

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
import logging
import string
import random
import verhoeff



class login(unittest.TestCase):
    logging.basicConfig(stream=sys.stdout , level=logging.DEBUG)
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
        self.a = string.ascii_letters + string.digits
        self.id1 = ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.id2 = ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))

        self.health_id = "H" + ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.ben_adhaar = []
        self.hus_aadhaar = []
        self.health_ids = []
        self.account_nos = []
        for i in range(10):
            self.accountno = ''.join(random.choice(string.digits) for i in range(18))
            if self.accountno not in self.account_nos:
                self.account_nos.append(self.accountno)
        for i in range(10):
            self.aadhaar1 = verhoeff.VerhoeffChecksum().generateVerhoeff(''.join(random.choice(string.digits) for i in range(1, 12)))
            if self.aadhaar1 not in self.ben_adhaar and int(self.aadhaar1[0]) != 0:
                self.ben_adhaar.append(self.aadhaar1)
        for i in range(20):
            self.aadhaar2 = verhoeff.VerhoeffChecksum().generateVerhoeff(
                ''.join(random.choice(string.digits) for i in range(1, 12)))
            if self.aadhaar2 not in self.hus_aadhaar and int(self.aadhaar2[0]) != 0 and self.aadhaar2 not in self.ben_adhaar:
                self.hus_aadhaar.append(self.aadhaar2)

        for i in range(10):
            self.health_id = "H" + ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
                random.choice(string.digits) for i in range(4))
            if self.health_id not in self.health_ids:
                self.health_ids.append(self.health_id)

        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")


    def test_01(self):

        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #
        print "Ben_aadhaar ids" , self.ben_adhaar
        logging.info("Aadhaar NUmber is : {}".format(self.ben_adhaar))
        print "Hus Aadhaar ids" , self.hus_aadhaar
        for i in range(1):
            emailid = self.driver.find_element_by_id("Email")
            emailid.send_keys("testautomation12@mailinator.com")
            time.sleep(3)
            print "Email entered"
            logging.info("Email Entered")
            password = self.driver.find_element_by_id("password")
            password.send_keys("P@ssw0rd2")
            print "Password entered"
            logging.info("Password Entered")
            time.sleep(3)
            self.driver.find_element_by_id("btnSubmit").click()
            time.sleep(4)
            # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
            print self.driver.title
            logging.info("Title : {}".format(self.driver.title))
            time.sleep(1)
            self.driver.find_element_by_id("btnNewbeneficiary").click()
            time.sleep(2)

            # Fill in all the valid details #

            self.driver.find_element_by_id("dpicker1").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[3]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[6]").click()
            time.sleep(1)
            print "Registration Date => ", self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute(
                "value")
            logging.info("Registration Date: {}".format(self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute(
                "value")))
            Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
            time.sleep(1)
            # print Aadhaar_avaialbilty_data[1].get_attribute('value')
            Aadhaar_avaialbilty_data[0].click()
            time.sleep(1)
            Aadhar_husband_availability = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
            Aadhar_husband_availability[0].click()
            time.sleep(1)
            self.driver.find_element_by_id("txtNameAsInAadhar").send_keys("Akshatha Hebbar")
            time.sleep(1)
            print "Beneficiary Name is " , self.driver.find_element_by_id("txtNameAsInAadhar").get_attribute("value")
            self.driver.find_element_by_id("txtAadhar").send_keys(self.ben_adhaar[i])
            time.sleep(1)
            print "Beneficiary ID is " , self.ben_adhaar[i]
            self.driver.find_element_by_xpath("//a[@id='BenAadhaarCheck']").click()
            time.sleep(2)

            self.driver.find_element_by_id("txtFNameAsInAadhaar").send_keys("Akash Hebbar")
            time.sleep(1)
            self.driver.find_element_by_id("txtFAadhar").send_keys(self.hus_aadhaar[i])
            time.sleep(1)
            print "Husband's aadhaar is " , self.hus_aadhaar[i]
            self.driver.find_element_by_xpath("//a[@id='HusbandAadhaarCheck']").click()
            time.sleep(2)
            print self.driver.find_element_by_xpath("//label[@id='lblBenAadharStatus']").text
            self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblBenAadharStatus']").text,
                            "Aadhaar is allowed for Registration")
            print self.driver.find_element_by_xpath("//label[@id='lblHusbandAadharStatus']").text
            self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblHusbandAadharStatus']").text,
                            "Aadhaar is allowed for Registration")

            self.driver.find_element_by_xpath("//input[@id='Phone']").send_keys("9990000016")
            time.sleep(1)
            self.driver.find_element_by_xpath("//select[@id='Category']/option[4]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='HealthId']").send_keys(self.health_ids[i])
            self.driver.find_element_by_xpath("//input[@id='dpicker2']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[3]").click()
            time.sleep(1)
            print "Last Menstrual Period (LMP) Date => ", self.driver.find_element_by_xpath(
                "//input[@id='dpicker2']").get_attribute("value")
            logging.info("LMP Date: {}".format(self.driver.find_element_by_xpath(
                "//input[@id='dpicker2']").get_attribute("value")))
            self.driver.find_element_by_xpath("//input[@id='dpicker3']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[6]").click()
            time.sleep(1)
            print "Date of Reg of MCP card at AWC/ Subcenter => ", self.driver.find_element_by_xpath(
                "//input[@id='dpicker3']").get_attribute("value")
            logging.info("Date of MCP: {}".format(self.driver.find_element_by_xpath(
                "//input[@id='dpicker3']").get_attribute("value")))
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
            self.driver.find_element_by_xpath("//input[@id='BankAccountNo']").send_keys(self.account_nos[i])
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='txtAccountHoldersName']").send_keys("Akshatha Hebbar")
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
            time.sleep(3)

            self.driver.find_element_by_link_text("Beneficiary").click()
            time.sleep(1)
            self.driver.find_element_by_link_text("Search Beneficiary").click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[1].click()
            time.sleep(2)
            self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.ben_adhaar[0])
            time.sleep(2)
            self.driver.find_element_by_id('btnSearch').click()
            time.sleep(2)
            print "Search by Aadhaar number validation"
            try:
                assert self.driver.find_element_by_link_text(
                    self.ben_adhaar[0]).text == self.ben_adhaar[0], "Search by Aadhaar for the number {} failed".format(
                    self.ben_adhaar)
            except:
                print "Aadhaar search failed"
            finally:
                print "Aadhaar search for the number {} is validated ".format(self.ben_adhaar)

            self.driver.find_element_by_link_text(
                self.ben_adhaar[0]).click()
            time.sleep(3)
            self.driver.find_element_by_link_text("WITHDRAW").click()
            time.sleep(3)
            self.driver.switch_to_alert().accept()
            time.sleep(3)
            self.driver.switch_to_alert().accept()

            self.driver.find_element_by_id("ancBenEdit").click()
            time.sleep(2)
            self.driver.find_element_by_id("AreaLocalitySector").clear()

            self.driver.find_element_by_id("AreaLocalitySector").send_keys("changed locality")

            self.driver.find_element_by_id("btnVerify").click()

            time.sleep(5)
            self.driver.switch_to_active_element()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
            time.sleep(2)
            self.driver.switch_to_alert().accept()
            time.sleep(5)
            self.driver.implicitly_wait(20)
            print self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/h5").text
            self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/h5").text,
                            " The beneficiary application form is sent for approval")
            time.sleep(3)
            # self.driver.find_element_by_xpath("//a[@class='dropdown']").click()
            # time.sleep(2)
            # self.driver.find_element_by_xpath("//a[@id='btnlogout']").click()
            # time.sleep(1)
            # self.assertIn("PRADHAN MANTRI MATRU VANDANA YOJANA", self.driver.title)
            # print self.driver.title
            # print "User Logged out Successfully"

    def tearDown(self):
        if self.driver.title == "PRADHAN MANTRI MATRU VANDANA YOJANA":
            time.sleep(20)
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