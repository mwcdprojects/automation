#!C:\Python27\python.exe
import sys
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

    def test_01_login_logout_user(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://test.rebuildkerala.in")
        self.assertIn("Rebuild Kerala", self.driver.title)
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        self.driver.find_elements_by_class_name("btn-signup")[0].click()
        name = raw_input("Enter Name")
        self.driver.find_element_by_id("Name").send_keys(name)
        time.sleep(2)
        email = raw_input("Enter Email")
        self.driver.find_element_by_id("EmailId").send_keys(email)
        time.sleep(2)
        phone = raw_input("Enter Mobile")
        self.driver.find_element_by_id("Phone").send_keys(phone)
        time.sleep(2)
        password = raw_input("Enter Password")
        self.driver.find_element_by_id("Password").send_keys(password)
        time.sleep(2)
        confirmpassword = raw_input("Enter Confirm Password")
        self.driver.find_element_by_id("ConfirmPassword").send_keys(confirmpassword)
        time.sleep(2)
        self.driver.find_element_by_id("BtnSave").click()
        time.sleep(3)
        print self.driver.find_element_by_xpath("//div[@class='col-lg-8 card py-4']/div/h4").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='col-lg-8 card py-4']/div/h4").text,
                        "Registration Succcess")

    def tearDown(self):
        if self.driver.title == "Rebuild Kerala":
            self.driver.quit()
        else:
            pass

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)
