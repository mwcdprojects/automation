#!C:\Python27\python.exe
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import string


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.fname = ""
        self.lname = ""
        self.emailaddr = ""
        self.mobile = "'"
        self.k = 1

    def test_01_login_user(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # self.driver.get('chrome://settings/clearBrowserData')
        self.driver.get("http://blbi-roots-test.southindia.cloudapp.azure.com/Account/Login")
        time.sleep(3)

        # ************************************* #
        # Login Details #
        # ************************************* #
        for i in range(1, 11):
            if self.k < 10:
                print "Value of k is " , self.k
            else:
                self.k = 1

            emailid = self.driver.find_element_by_id("Email")
            emailid.send_keys("demotlkuser@gmail.com")
            time.sleep(3)
            print "Email entered"
            password = self.driver.find_element_by_id("Password")
            password.send_keys("demotlkuser")
            print "Password entered"
            time.sleep(3)

            self.driver.find_element_by_xpath("//input[@class='button button-block']").click()
            self.assertIn("DashboardTaluk - Root Reforms", self.driver.title)
            time.sleep(2)
            self.driver.find_element_by_id("tab3").click()
            time.sleep(2)

            self.fname = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            self.driver.find_element_by_id("FName").send_keys(self.fname)
            print "First Name is " , self.fname
            time.sleep(2)
            self.lname = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            self.driver.find_element_by_id("LName").send_keys(self.lname)
            print "Last Name is ", self.lname
            time.sleep(2)
            self.emailaddr = self.fname + "." + self.lname + "@gmail.com"
            self.driver.find_element_by_id("email").send_keys(self.emailaddr)
            print "Email Address is " , self.emailaddr
            time.sleep(2)
            self.driver.find_element_by_id("password").send_keys("p@ssw0rd")
            time.sleep(2)
            self.mobile = ''.join(random.choice(string.digits) for _ in range(10))
            for j in range(20):
                if int(self.mobile[0]) == 0:
                    self.mobile = ''.join(random.choice(string.digits) for _ in range(10))
                    print "Mobile Number new", self.mobile
                else:
                    break

            self.driver.find_element_by_id("Mob").send_keys(self.mobile)
            print "Mobile Number is " , self.mobile
            self.driver.find_element_by_xpath("//select[@id='createUser_AreaId']/option["+str(self.k+1)+"]").click()
            self.k = self.k + 1
            self.driver.find_element_by_id("Remarks").send_keys("Test Remarks")
            time.sleep(2)
            self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSave").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[@class='nbar dropdown-toggle']").click()
            time.sleep(2)
            self.driver.find_element_by_id("btnlogoff").click()
            print "User Logged out Successfully"

            # Login as pac user

            emailid = self.driver.find_element_by_id("Email")
            emailid.send_keys(self.emailaddr)
            time.sleep(3)
            print "Email entered"
            password = self.driver.find_element_by_id("Password")
            password.send_keys("p@ssw0rd")
            print "Password entered"
            time.sleep(3)

            self.driver.find_element_by_xpath("//input[@class='button button-block']").click()
            self.assertIn("Dashboard - Root Reforms", self.driver.title)
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='EntryDetails_AuditStatus']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='EntryDetails_FinancialStatus']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='EntryDetails_Computerized']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='EntryDetails_Within1KVillageLimit']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='EntryDetails_BDPStatus']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='RbPOYes']")[0].click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='PON']").send_keys("Org Info Test")
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='EntryDetails_MOUSignStatus']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='RbNBYes']")[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath("//input[@id='BDate']")[0].click()
            time.sleep(2)

            self.driver.find_element_by_xpath("//input[@id='EntryDetails_CorpusAmount']").send_keys("50000")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='EntryDetails_TurnOver']").send_keys("60000")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='EntryDetails_ProfitAmount']").send_keys("20000")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='EntryDetails_IncomeAmount']").send_keys("20000")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='EntryDetails_MiscInfo']").send_keys("Misc Info Test")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='btnSave']").click()
            time.sleep(2)
            # self.driver.switch_to_frame()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@id='success']/div/div/div/center/button").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//div[@id='gridview1']/div/table/tbody/tr/td[26]").click()
            #self.driver.find_element_by_xpath("//a[@id='Edit_57']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[@class='nbar dropdown-toggle']").click()
            time.sleep(2)
            self.driver.find_element_by_id("btnlogoff").click()
            print "User Logged out Successfully"

            # Approval

            emailid = self.driver.find_element_by_id("Email")
            emailid.send_keys("demotlkuser@gmail.com")
            time.sleep(3)
            print "Email entered"
            password = self.driver.find_element_by_id("Password")
            password.send_keys("demotlkuser")
            print "Password entered"
            time.sleep(3)

            self.driver.find_element_by_xpath("//input[@class='button button-block']").click()
            self.assertIn("DashboardTaluk - Root Reforms", self.driver.title)
            time.sleep(2)
            self.driver.find_element_by_id("tab1").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@id='gridview1']/div/table/tbody/tr/td[24]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//div[@id='Prompt_YesNo']/div/div/div/section/div/button").click()
            time.sleep(3)

            self.driver.find_element_by_xpath("//a[@class='nbar dropdown-toggle']").click()
            time.sleep(2)
            self.driver.find_element_by_id("btnlogoff").click()
            print "User Logged out Successfully"



    def tearDown(self):
        if self.driver.title == "Log in - Root Reforms":
            self.driver.quit()
        else:
            self.driver.find_element_by_xpath("//a[@class='nbar dropdown-toggle']").click()
            time.sleep(2)
            self.driver.find_element_by_id("btnlogoff").click()
            print "User Logged out Successfully"
            self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)





