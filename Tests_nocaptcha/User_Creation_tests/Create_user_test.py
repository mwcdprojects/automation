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
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # ************************************* #
        # Invalid email and password validation #
        # ************************************* #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("pmmvy.itops@billionlives.in")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("Pmmvy@it0ps")
        print "Password entered"
        time.sleep(3)

        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Block Field Functionary Mapping - MWCD Backoffice", self.driver.title)
        print self.driver.title
        self.driver.find_element_by_xpath("//div[@id='main-menu']/div/ul/li/a/b").click()
        self.driver.find_element_by_link_text("Users").click()
        self.driver.find_element_by_link_text("Create New User").click()

        # Enter details for User creation
        self.driver.find_element_by_id("Email").click()
        time.sleep(1)
        self.driver.find_element_by_id("Email").send_keys("dataentry123@mailinator.com")
        time.sleep(1)
        self.driver.find_element_by_id("FirstName").click()
        time.sleep(1)
        self.driver.find_element_by_id("FirstName").send_keys("dataentry")
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("P@ssw0rd1")
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").clear()
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").send_keys("P@ssw0rd1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='radDataEntryLevel']").click()
        time.sleep(1)
        self.driver.find_element_by_id("ContactPhone").send_keys("9322345532")
        time.sleep(1)
        states = self.driver.find_elements_by_xpath("//select[@class='ddlLookupState form-control ea-triggers-bound']/option")
        [each for each in states if "ASSAM" in each.text][0].click()
        time.sleep(2)
        districts = self.driver.find_elements_by_xpath("//select[@class='ddlLookupDistrict form-control ea-triggers-bound']/option")
        [each1 for each1 in districts if 'DHEMAJI' in each1.text][0].click()
        time.sleep(2)
        blocks = self.driver.find_elements_by_xpath("//select[@class='ddlLookupCdpo form-control ea-triggers-bound']/option")
        [each2 for each2 in blocks if "Dhemaji" in each2.text][0].click()
        time.sleep(2)
        self.driver.find_element_by_id("btnSubmit").click()



    def tearDown(self):
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





