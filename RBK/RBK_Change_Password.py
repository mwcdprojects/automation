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
        self.driver.find_element_by_name("EmailId").send_keys("archena@billionlives.in")
        time.sleep(1)
        self.driver.find_element_by_name("Pwd").send_keys("P@ssw0rd")
        time.sleep(1)
        self.driver.find_element_by_id("BtnLogin").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//ul[@class='nav navbar-nav navbar-right']/li/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Change Password").click()
        time.sleep(2)
        self.driver.find_element_by_id("OldPassword").clear()
        # Invalid old password
        self.driver.find_element_by_id("OldPassword").send_keys("P@ss")
        time.sleep(2)
        self.driver.find_element_by_id("NewPassword").send_keys("P@ssw0rd2")
        time.sleep(2)
        self.driver.find_element_by_id("ConfirmNewPassword").send_keys("P@ssw0rd2")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='col-sm-12']/button").click()
        time.sleep(2)
        #print self.driver.find_element_by_xpath("//div[@class='col-sm-12']/span").text
        self.assertTrue(self.driver.find_element_by_xpath("//*[contains(text(), 'The value entered for the Old Password field is not correct')]"))

        #New password and confirm password do not match

        self.driver.find_element_by_id("OldPassword").clear()
        # Invalid old password
        self.driver.find_element_by_id("OldPassword").send_keys("P@ssw0rd1")
        time.sleep(2)
        self.driver.find_element_by_id("NewPassword").send_keys("P@ssw0rd31")
        time.sleep(2)
        self.driver.find_element_by_id("ConfirmNewPassword").send_keys("P@ssw0rd4")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='col-sm-12']/button").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//div[@class='col-sm-12']/span").text
        #self.assertTrue(self.driver.find_element_by_xpath("//div[@class='col-sm-12']/span").text , "\'ConfirmNewPassword\' and \'NewPassword\' do not match.")
        #self.assertTrue(self.driver.find_element_by_xpath("//*[contains(text(), '\'ConfirmNewPassword\' and \'NewPassword\' do not match.')]"))

        self.driver.find_element_by_id("OldPassword").clear()
        self.driver.find_element_by_id("OldPassword").send_keys("P@ssw0rd1")
        time.sleep(2)
        self.driver.find_element_by_id("NewPassword").clear()
        self.driver.find_element_by_id("NewPassword").send_keys("P@ssw0rd31")
        time.sleep(2)
        self.driver.find_element_by_id("ConfirmNewPassword").clear()
        self.driver.find_element_by_id("ConfirmNewPassword").send_keys("P@ssw0rd31")
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='col-sm-12']/button").click()
        time.sleep(2)

        print self.driver.find_element_by_xpath("//div[@class='col-lg-8 card py-4']/div/h4").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='col-lg-8 card py-4']/div/h4").text,
                        "Password Changed Succcessfully")

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
