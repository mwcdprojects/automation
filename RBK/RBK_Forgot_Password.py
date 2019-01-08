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

        self.driver.find_element_by_class_name("btn-login").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Forgot Password").click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("archena@billionlives.in")
        time.sleep(1)
        self.driver.find_element_by_id("BtnSubmit").click()
        time.sleep(2)
        print self.driver.find_element_by_id("lblSuccess").text
        self.assertTrue(self.driver.find_element_by_id("lblSuccess").text , "Password reset link sent via email.")




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
