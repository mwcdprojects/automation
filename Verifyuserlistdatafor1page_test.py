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

    def test_01_check_created_account_onepage(self):

        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("block_kalpetta@mailinator.com")
        # time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print "Password entered"
        time.sleep(3)
        captcha_text = self.driver.find_element_by_id("CaptchaInputText")
        captcha_text.send_keys("")
        print "Enter the text displayed from the captcha image manually"
        time.sleep(5)
        WebDriverWait(self.driver, 900).until(EC.visibility_of_element_located((By.ID, "CaptchaInputText")))
        print "Text found"
        self.driver.find_element_by_id("CaptchaInputText").send_keys()
        time.sleep(4)
        self.driver.find_element_by_id("btnSubmit").click()
        #self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title
        self.driver.get("http://mwcd.fundright.in/backoffice/useraccount/list")
        try:
            if self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul").is_displayed():
                self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul")
                print self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul").text
                values = self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul").text
                print "values", type(values.split("\n"))
                pages = int(values.split("\n")[-2])
        except NoSuchElementException:
                pages = 1
        print pages
        flag = 0
        for i in range(1, pages + 1):
            print "Verifying in page: ", i
            if self.driver.find_elements_by_xpath("//*[contains(text(), 'dataentry_kalpetta@mailinator.com')]"):
                print "New User Account found"
                flag = 1
                break
            self.driver.find_element_by_link_text(str(i + 1)).click()
        self.assertEqual(flag, 1, "New user created not found in the User List")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)





