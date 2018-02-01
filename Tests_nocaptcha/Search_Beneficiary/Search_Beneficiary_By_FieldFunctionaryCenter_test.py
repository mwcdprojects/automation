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

    def test_01_Beneficiary_Details_Fieldfunctionary(self):
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
        password.send_keys("P@ssw0rd1")
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
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        # *********************************** #
        # Search Beneficiary validation       #
        # Search By Field Functionary number  #
        # *********************************** #

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("523834271501").click()
        time.sleep(1)
        print "Beneficiary Name is " , self.driver.find_element_by_id("NameAsInAadhar").get_attribute('value')
        print "Beneficiary Aadhaar Number is " ,self.driver.find_element_by_id("AadharNo").get_attribute('value')
        print "Beneficiary Alternate Number is ",self.driver.find_element_by_id("BeneficiaryAlternatenumber").get_attribute('value')
        print "Beneficairy Contact Number is " , self.driver.find_element_by_id("Phone").get_attribute('value')
        print "Beneficiary Husband Name is " , self.driver.find_element_by_id("FNameAsInAadhar").get_attribute('value')
        print "Field functionary is " , self.driver.find_element_by_id("Anganvaadi").get_attribute('value')
        print "Village is " , self.driver.find_element_by_id("VillageName").get_attribute('value')
        print "Block is " , self.driver.find_element_by_id("Block").get_attribute('value')
        print "District " ,self.driver.find_element_by_id("District").get_attribute('value')
        print "State " , self.driver.find_element_by_id("State").get_attribute('value')
        print "Details Entered by " , self.driver.find_element_by_id("EnteredbyUser").get_attribute('value')
        print "Details Verified by ",self.driver.find_element_by_id("VerifiedbyUser").get_attribute('value')
        print "Bank is " , self.driver.find_element_by_id("BankName").get_attribute('value')
        print "Bank Account number is ",self.driver.find_element_by_id("BankAccountNo").get_attribute('value')

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
