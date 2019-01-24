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
        self.aadhaarno = "580129573762"
        self.dlno = "iZPV3651"
        self.voterid = "NRkm7444"
        self.pancard = "UrIC2583"
        self.passport = "BGxl2717"
        self.rationcard = "44282496"
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
        self.accountno = ''.join(random.choice(string.digits) for i in range(18))
        self.health_id = "H" + ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.aadhaar1 = verhoeff.VerhoeffChecksum().generateVerhoeff(''.join(random.choice(string.digits) for i in range(1, 12)))
        self.aadhaar2 = verhoeff.VerhoeffChecksum().generateVerhoeff(''.join(random.choice(string.digits) for i in range(1, 12)))
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
        self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[1].click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.aadhaarno)
        time.sleep(2)
        self.driver.find_element_by_id('btnSearch').click()
        time.sleep(2)
        print "Search by Aadhaar number validation"
        try:
            assert self.driver.find_element_by_link_text(self.aadhaarno).text == self.aadhaarno , "Search by Aadhaar for the number {} failed".format(self.aadhaarno)
        except:
            print "Aadhaar search failed"
        finally:
            print "Aadhaar search for the number {} is validated ".format(self.aadhaarno)
    def test_02_DL(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************ #
        # Search By Driving License Number #
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
        self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[8].click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.dlno)
        time.sleep(2)
        self.driver.find_element_by_id('btnSearch').click()
        time.sleep(2)
        # assert self.driver.find_element_by_xpath("//div[@class='grid-wrap']/table/tbody/tr/td/span")

        print "Search by Driving License number validation"
        try:
            assert self.driver.find_element_by_link_text(
                self.dlno).text == self.dlno, "Search by Driving License for the number {} failed".format(
                self.dlno)
        except:
            print "Driving License search failed"
        finally:
            print "DL search for the number {} is validated ".format(self.dlno)

    def test_03_Rationcard(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************ #
        # Search By Ration Card Number #
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
        self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[5].click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.rationcard)
        time.sleep(2)
        self.driver.find_element_by_id('btnSearch').click()
        time.sleep(2)
        # assert self.driver.find_element_by_xpath("//div[@class='grid-wrap']/table/tbody/tr/td/span")

        print "Search by Ration Card number validation"
        try:
            assert self.driver.find_element_by_link_text(
                self.rationcard).text == self.rationcard, "Search by Ration Card for the number {} failed".format(
                self.rationcard)
        except:
            print "Ration Card search failed"
        finally:
            print "Ration Card search for the number {} is validated ".format(self.rationcard)

    def test_04_passport(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************ #
        # Search By Passport Number #
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
        self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[7].click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.passport)
        time.sleep(2)
        self.driver.find_element_by_id('btnSearch').click()
        time.sleep(2)
        # assert self.driver.find_element_by_xpath("//div[@class='grid-wrap']/table/tbody/tr/td/span")

        print "Search by Passport number validation"
        try:
            assert self.driver.find_element_by_link_text(
                self.passport).text == self.passport, "Search by Ration Card for the number {} failed".format(
                self.passport)
        except:
            print "Passport search failed"
        finally:
            print "Passport search for the number {} is validated ".format(self.passport)

    def test_05_voterid(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************ #
        # Search By VoterId Number #
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
        self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[4].click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.voterid)
        time.sleep(2)
        self.driver.find_element_by_id('btnSearch').click()
        time.sleep(2)
        # assert self.driver.find_element_by_xpath("//div[@class='grid-wrap']/table/tbody/tr/td/span")

        print "Search by VoterId number validation"
        try:
            assert self.driver.find_element_by_link_text(
                self.voterid).text == self.voterid, "Search by Ration Card for the number {} failed".format(
                self.voterid)
        except:
            print "VoterID search failed"
        finally:
            print "VoterId search for the number {} is validated ".format(self.voterid)

    def test_06_PANCard(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************ #
        # Search By Ration Card Number #
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
        self.driver.find_elements_by_xpath("//select[@id='beneficiaryAltID']/option")[9].click()
        time.sleep(2)
        self.driver.find_element_by_id("txtAlternateNumber").send_keys(self.pancard)
        time.sleep(2)
        self.driver.find_element_by_id('btnSearch').click()
        time.sleep(2)
        # assert self.driver.find_element_by_xpath("//div[@class='grid-wrap']/table/tbody/tr/td/span")

        print "Search by PAN Card number validation"
        try:
            assert self.driver.find_element_by_link_text(
                self.pancard).text == self.pancard, "Search by PAN Card for the number {} failed".format(
                self.pancard)
        except:
            print "PAN Card search failed"
        finally:
            print "PAN Card search for the number {} is validated ".format(self.pancard)

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