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
    """
    def test_01_enter_user_details(self):

        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("block_sulthanbathery@mailinator.com")
        time.sleep(3)
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
        #self.driver.find_element_by_id("CaptchaInputText").send_keys()
        time.sleep(4)
        self.driver.find_element_by_id("btnSubmit").click()
        self.assertIn("Approval Queue - MWCD Backoffice" , self.driver.title)
        print self.driver.title
        self.driver.find_element_by_xpath("//div[@id='main-menu']/div/ul/li/a/b").click()
        self.driver.find_element_by_link_text("Users").click()
        self.driver.find_element_by_link_text("Create New User").click()


        # ********************** #
        # Email id validation #
        # ********************** #

        self.driver.find_element_by_id("Email").click()
        time.sleep(1)
        self.driver.find_element_by_id("Email").send_keys("test")
        time.sleep(1)
        self.driver.find_element_by_id("FirstName").click()
        self.assertIn(self.driver.find_element_by_id("Email-error").text,"The Email field is not a valid e-mail address.")
        time.sleep(1)
        print self.driver.find_element_by_id("Email-error").text
        self.driver.find_element_by_id("Email").click()
        time.sleep(1)
        self.driver.find_element_by_id("Email").clear()
        time.sleep(1)
        self.driver.find_element_by_id("FirstName").click()

        self.assertIn(self.driver.find_element_by_id("Email-error").text,
                      "Required")
        print self.driver.find_element_by_id("Email-error").text
        self.driver.find_element_by_id("Email").clear()
        time.sleep(1)
        self.driver.find_element_by_id("Email").send_keys("test089@example.com")
        time.sleep(1)

        # ********************** #
        # FirstName validation #
        # ********************** #

        self.driver.find_element_by_id("FirstName").clear()
        time.sleep(1)
        self.driver.find_element_by_id("FirstName").send_keys("test 123")
        time.sleep(1)
        self.driver.find_element_by_id("password").click()
        time.sleep(1)
        self.assertIn(self.driver.find_element_by_id("FirstName-error").text, "Please enter valid Name")
        time.sleep(1)
        print self.driver.find_element_by_id("FirstName-error").text
        self.driver.find_element_by_id("FirstName").clear()
        time.sleep(1)
        self.driver.find_element_by_id("password").click()
        time.sleep(1)

        self.assertIn(self.driver.find_element_by_id("FirstName-error").text,
                      "Required")
        print self.driver.find_element_by_id("FirstName-error").text
        self.driver.find_element_by_id("FirstName").clear()
        time.sleep(1)
        self.driver.find_element_by_id("FirstName").send_keys("test test")
        time.sleep(1)

        # ********************** #
        # Password validation #
        # ********************** #

        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("pass")
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").click()
        self.assertIn(self.driver.find_element_by_id("password-error").text , "The Password must be at least 6 characters long.")
        print self.driver.find_element_by_id("password-error").text
        self.driver.find_element_by_id("password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("password123")
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").clear()
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").send_keys("password123")
        time.sleep(1)

        # ********************** #
        # Phone Number validation #
        # ********************** #

        self.driver.find_element_by_id("ContactPhone").send_keys("ddsad")
        time.sleep(1)
        self.driver.find_element_by_id("Department").click()
        time.sleep(1)
        self.assertIn(self.driver.find_element_by_id("ContactPhone-error").text , "Enter valid Phone number.")
        time.sleep(1)
        print self.driver.find_element_by_id("ContactPhone-error").text
        self.driver.find_element_by_id("ContactPhone").clear()
        time.sleep(1)
        self.driver.find_element_by_id("ContactPhone").send_keys("9322345532")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(1)
        self.assertIn(self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/div/span").text , " Password must be between 8 and 14 characters and Must be a combination of letters,numbers and special characters ")
        print self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/div/span").text
        time.sleep(1)
        self.driver.find_element_by_id("password").click()
        time.sleep(1)
        self.driver.find_element_by_id("password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys("Password1234!@#$")
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").clear()
        time.sleep(1)
        self.driver.find_element_by_id("confirmpassword").send_keys("Password1234!@#$")
        time.sleep(1)
        self.driver.find_element_by_id("Department").clear()
        time.sleep(1)
        self.driver.find_element_by_id("Department").send_keys("fund")
        time.sleep(1)
        self.driver.find_element_by_id("Designation").clear()
        time.sleep(1)
        self.driver.find_element_by_id("Designation").send_keys("supervisor")
        time.sleep(1)
        self.driver.find_element_by_id("ContactAddress").clear()
        time.sleep(1)
        self.driver.find_element_by_id("ContactAddress").send_keys("Kerela")
        time.sleep(1)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(3)

        # ************************************************************** #
        # User Saved Page Navigation check and created account validation#
        # ************************************************************** #

        self.assertIn("List - MWCD Backoffice", self.driver.title)
        print self.driver.title
        self.assertIn(self.driver.find_element_by_xpath("/html/body/div[2]/div/form/p").text , "User Saved Successfully")
        print self.driver.find_element_by_xpath("/html/body/div[2]/div/form/p").text

    """
    def test_02_check_created_account(self):

        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("block_sulthanbathery@mailinator.com")
        #time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print "Password entered"
        #time.sleep(3)
        captcha_text = self.driver.find_element_by_id("CaptchaInputText")
        captcha_text.send_keys("")
        print "Enter the text displayed from the captcha image manually"
        time.sleep(3)
        WebDriverWait(self.driver, 900).until(EC.visibility_of_element_located((By.ID, "CaptchaInputText")))
        print "Text found"
        # self.driver.find_element_by_id("CaptchaInputText").send_keys()
        #time.sleep(4)
        self.driver.find_element_by_id("btnSubmit").click()
        self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title
        self.driver.get("http://mwcd.fundright.in/backoffice/useraccount/list")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul/li[3]/a")
        print self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul/li[3]/a").text
        self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div/ul/li[3]/a").click()
        #if self.driver.find_elements_by_xpath("//*[contains(text(), 'test007@example.com')]"):
         #   print "New Account found"
        values = self.driver.find_element_by_xpath("/html/body/div[2]/div/form/div[2]/div/div/div/div/div")
        pages =  int(values.text.split("\n")[-1])
        print pages
        flag = 0
        for i in range(1,pages+1):
            print "Verifying in page: ", i
            self.driver.find_element_by_link_text(str(i)).click()
            if self.driver.find_elements_by_xpath("//*[contains(text(), 'test0844@example.com')]"):
                print "New User Account found"
                flag = 1
                break
        self.assertEqual(flag , 1, "New user created not found in the User List")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    #print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails" , len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)





