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
        self.src = self.driver.page_source
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""

    def test_01_checkuserdata(self):

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
        bodyText = self.driver.find_element_by_tag_name('body').text

        if pages == 1:
            if "dataentry_kalpetta@mailinator.com" in bodyText:
                print "User found!!"
                flag = 1
        else:
            for i in range(1, pages + 1):
                print "Verifying in page: ", i
                if self.driver.find_elements_by_xpath("//*[contains(text(), 'dataentry_kalpetta@mailinator.com')]"):
                    print "User found!!"
                    flag = 1
                    break
                self.driver.find_element_by_link_text(str(i + 1)).click()
        self.assertEqual(flag, 1, "User not found in the User List")

        # *********************************** #
        # User Activate/Deactivate validation #
        # *********************************** #

        self.driver.find_element_by_xpath("//button[@value='10139']").click()
        time.sleep(3)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        print self.driver.find_element_by_xpath("//button[@value='10139']").text

        # ***************************** #
        # User Account - Reset Password #
        # ***************************** #

        self.driver.find_element_by_link_text("Reset Password").click()
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[3]/div/input[2]").click()
        print self.driver.title
        time.sleep(2)
        self.driver.find_element_by_link_text("Reset Password").click()
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.find_element_by_id("newPassword").send_keys("")
        self.driver.find_element_by_id("confirmPassword").send_keys("")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)
        self.assertIn(self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[1]/div/div/span").text,"Password must be between 8 and 14 characters and Must be a combination of letters,numbers and special characters")
        self.driver.find_element_by_id("newPassword").send_keys("P@ssw0rd2")
        self.driver.find_element_by_id("confirmPassword").send_keys("P@ssw0rd")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)
        self.assertIn(self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div/span").text,"The password and confirmation password do not match")
        self.driver.find_element_by_id("newPassword").send_keys("P@ssw0rd2")
        self.driver.find_element_by_id("confirmPassword").send_keys("P@ssw0rd2")
        self.driver.find_element_by_id("btnSubmit").click()
        #self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[3]/div/input[2]").click()
        time.sleep(3)
        self.assertIn(self.driver.find_element_by_xpath("/html/body/div[2]/div/form/p").text , "Password Changed Successfully")

        # ******************************** #
        # User Account - Edit user Details #
        # ******************************** #
        self.driver.find_element_by_link_text("Edit").click()
        time.sleep(1)
        #self.driver.find_element_by_id("Email").clear()
        #time.sleep(1)
        #self.driver.find_element_by_id("Email").send_keys("dataentry2@kalpetta.com")
        #time.sleep(1)
        self.driver.find_element_by_id("FirstName").clear()
        self.driver.find_element_by_id("FirstName").send_keys("Alok")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit").click()



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





