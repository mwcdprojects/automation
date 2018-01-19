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

    def test_01_forgot_password(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # ************************** #
        # Forgot Password validation #
        # ************************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("block_panamaram@mailinator.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print "Password entered"
        time.sleep(3)
        """
        captcha_text = self.driver.find_element_by_id("CaptchaInputText")
        captcha_text.send_keys("")
        print "Enter the text displayed from the captcha image manually"
        time.sleep(5)
        WebDriverWait(self.driver, 900).until(EC.visibility_of_element_located((By.ID, "CaptchaInputText")))
        print "Text found"
        self.driver.find_element_by_id("CaptchaInputText").send_keys()
        time.sleep(4)
        """
        self.driver.find_element_by_id("btnResetPassword").click()
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)


        # **************** #
        # Login validation #
        # **************** #
        self.driver.find_element_by_id("Email").clear()
        time.sleep(1)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("block_panamaram@mailinator.com")
        time.sleep(3)
        print "Email entered"
        self.driver.find_element_by_id("password").clear()
        time.sleep(1)
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print "Password entered"
        time.sleep(3)
        """
        captcha_text = self.driver.find_element_by_id("CaptchaInputText")
        captcha_text.send_keys("")
        print "Enter the text displayed from the captcha image manually"
        time.sleep(5)
        WebDriverWait(self.driver, 900).until(EC.visibility_of_element_located((By.ID, "CaptchaInputText")))
        print "Text found"
        self.driver.find_element_by_id("CaptchaInputText").send_keys()
        time.sleep(4)
        """
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        #self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        # **************** #
        # Logout validation #
        # **************** #
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"main-menu\"]/div/ul[5]/li/a").click()
        time.sleep(2)
        self.driver.find_element_by_id("btnlogout").click()
        time.sleep(1)
        self.assertIn("PRADHAN MANTRI MATRU VANDANA YOJANA" , self.driver.title)
        print self.driver.title
        print "User Logged out Successfully"

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
