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

    def test_01_login_card_list_view(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://test.rootsreforms.in")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        login = self.driver.find_element_by_link_text("Login").click()
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("lpuser1@mailinator.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("Password")
        password.send_keys("p@ssw0rd")
        print "Password entered"
        time.sleep(3)
        # Login button
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/center/div/div/form/div[2]/div[1]/center/button").click()
        time.sleep(4)
        self.assertIn("LP Board - Roots", self.driver.title)
        print self.driver.title
        self.driver.find_element_by_link_text("List View").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Card View").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("List View").click()
        time.sleep(3)
        # Mark Selected profiles as Exclusive
        #self.driver.find_element_by_id("chk_1").click()
        #self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/div/div[2]/div/div/div/table/tbody/tr[2]/td[9]/span/input[1]").click()
        #time.sleep(2)
        #self.driver.find_element_by_id("chk_2").click()
        #self.driver.find_element_by_xpath(
         #   "/html/body/div[2]/div/div[2]/div/form/div/div[2]/div/div/div/table/tbody/tr[2]/td[9]/span/input[1]").click()
        #time.sleep(4)
        #self.driver.find_element_by_link_text("Mark selected Profiles as Exclusive").click()
        self.driver.find_element_by_link_text("View").click()
        time.sleep(2)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(3)
        self.driver.find_elements_by_xpath(
            "//div[@class='col-lg-12 col-md-12 col-sm-12 panel panel-body text-center']/button")[0].click()
        self.driver.switch_to_alert().accept()
        time.sleep(3)
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element_by_link_text("Exclusive Marked").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Release").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(3)
        self.driver.find_element_by_link_text("Dashboard").click()
        time.sleep(2)



        # **************** #
        # Logout validation #
        # **************** #
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[2]/a/i").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[2]/form/a/b").click()
        time.sleep(1)
        self.assertIn("Roots Reforms" , self.driver.title)
        print self.driver.title
        print "User Logged out Successfully"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)
