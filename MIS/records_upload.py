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

    def test_01_login_user(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # self.driver.get('chrome://settings/clearBrowserData')
        self.driver.get("http://blbi-roots-test.southindia.cloudapp.azure.com/Account/Login")
        time.sleep(3)

        # ************************************* #
        # Login Details #
        # ************************************* #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("iogdl.lyvdm@gmail.com")
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
        self.driver.find_element_by_xpath("//input[@id='RbNBYes']").click()
        time.sleep(2)
        self.driver.find_element_by_name("EntryDetails.BusinessName").send_keys("Test Business")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='BDate']").send_keys("07/11/2018")
        time.sleep(2)
        self.driver.find_element_by_id("Emp").send_keys("0")
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
        #self.driver.switch_to_frame()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@id='success']/div/div/div/center/button").click()
        time.sleep(3)


    def tearDown(self):
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





