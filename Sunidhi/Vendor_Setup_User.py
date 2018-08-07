#!C:\Python27\python.exe

"""
StakeHolder - Vendor Setup User.
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
        self.driver.find_element_by_link_text("Vendors").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Users").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='btn btn-success pull-right']").click()
        time.sleep(2)
        self.driver.find_element_by_id("Name").send_keys("Vendor User Name")
        time.sleep(2)
        self.driver.find_element_by_id("Phone").send_keys("9987654322")
        time.sleep(2)
        self.driver.find_element_by_id("EmailId").send_keys("testvendoruser1@mailinator.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='RoleID']/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_id("Password").send_keys("p@ssw0rd")
        time.sleep(2)
        self.driver.find_element_by_id("ConfirmPassword").send_keys("p@ssw0rd")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
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
