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

    def test_01_Generate_report(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print "Password entered"
        time.sleep(3)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        # ***************************** #
        # Report validation #
        # Filter by validation      #
        # ***************************** #

        self.driver.find_element_by_link_text("Report").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Payments Report").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='btn btn-primary']").click()
        time.sleep(1)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        self.driver.find_element_by_xpath("//select[@id='Month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Year']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Sector']/option[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='FieldFunctionary']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='btn btn-primary']").click()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//input[@class='btn add-new-btn hidden-print pull-right']").click()
        #time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//table[@class='table table-bordered']/tbody/tr")
        for each in table_data:
            print each.text

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