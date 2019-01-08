#!C:\Python27\python.exe

"""
StakeHolder - FP Setup.
"""
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""

    def test_01_Initiative_Creation(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://sunidhi-test.fundright.in/backoffice/useraccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        login = self.driver.find_element_by_id("Email").send_keys("superadmin@mailinator.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("Password")
        password.send_keys("p@ssw0rd")
        print "Password entered"
        time.sleep(3)
        # Login button
        self.driver.find_element_by_id("BtnLogin").click()
        time.sleep(4)
        self.assertIn("SUNIDHI-CSR", self.driver.title)
        print self.driver.title
        self.driver.find_element_by_xpath("//div[@class = 'sidebar-nav navbar-collapse']/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Fund Providers").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='btn btn-success pull-right btnWriteAction']").click()
        time.sleep(2)
        self.driver.find_element_by_id("ClientName").send_keys("Automation-Trust Name")
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='TrustID']/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_id("ContactName").send_keys("FP Name1")
        time.sleep(2)
        self.driver.find_element_by_id("ContactPhone").send_keys("9987621344")
        time.sleep(2)
        self.driver.find_element_by_id("ContactEmail").send_keys("FP1@mailinator.com")
        time.sleep(2)
        self.driver.find_element_by_id("ClientDescription").send_keys("FP Description")
        time.sleep(2)
        self.driver.find_element_by_id("ContactAddress").send_keys("FP Address")
        time.sleep(2)
        self.driver.find_element_by_id("State").send_keys("Bangalore")
        time.sleep(2)
        self.driver.find_element_by_id("PinCode").send_keys("631001")
        time.sleep(2)
        self.driver.find_element_by_id("save").click()
        time.sleep(4)




        # **************** #
        # Logout validation #
        # **************** #
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/nav/ul/li[2]/a/i[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/nav/ul/li[2]/ul/li[4]/a").click()
        time.sleep(1)
        self.assertIn("SUNIDHI" , self.driver.title)
        print self.driver.title
        print "User Logged out Successfully"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)
