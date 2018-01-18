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
        self.bodyText = self.driver.find_element_by_tag_name('body').text

    def test_01_login_logout_user(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

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
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        #self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        # **************** #
        # Change Password validation #
        # **************** #
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"main-menu\"]/div/ul[5]/li/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Change Password").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='Cancel']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"main-menu\"]/div/ul[5]/li/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Change Password").click()
        time.sleep(1)
        self.driver.find_element_by_id("oldPassword").send_keys("P@ss")
        self.driver.find_element_by_id("newPassword").send_keys("P@ssw0rd")
        self.driver.find_element_by_id("confirmPassword").send_keys("P@ssw0rd")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit")
        time.sleep(1)
        self.assertIn(self.bodyText , "Wrong Password")
        time.sleep(1)
        self.driver.find_element_by_id("oldPassword").send_keys("P@ssw0rd")
        self.driver.find_element_by_id("newPassword").send_keys("P@ssw0rd")
        self.driver.find_element_by_id("confirmPassword").send_keys("P@ssw0rd")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(1)
        self.assertIn(self.bodyText, "This password was used before")
        time.sleep(1)
        self.driver.find_element_by_id("oldPassword").send_keys("P@ssw0rd")
        self.driver.find_element_by_id("newPassword").send_keys("P@ss")
        self.driver.find_element_by_id("confirmPassword").send_keys("P@ss")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(1)
        self.assertIn(self.bodyText, "Password must be between 8 and 14 characters and Must be a combination of letters,numbers and special characters")
        self.driver.find_element_by_id("oldPassword").send_keys("P@ssw0rd")
        self.driver.find_element_by_id("newPassword").send_keys("P@ssw0rd1")
        self.driver.find_element_by_id("confirmPassword").send_keys("P@ssw0rd1")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(1)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        print self.driver.title

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