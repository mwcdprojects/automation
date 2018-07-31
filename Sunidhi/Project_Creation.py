#!C:\Python27\python.exe
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""

    def test_01_Project_Creation(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://sunidhi-test.fundright.in/backoffice/useraccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        login = self.driver.find_element_by_id("Email").send_keys("superadmin@mailinator.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("Password")
        password.send_keys("p@ssw0rd")
        print "Password entered"
        time.sleep(3)
        # Login button
        self.driver.find_element_by_id("BtnLogin").click()
        time.sleep(4)
        self.assertIn("SUNIDHI-CSR", self.driver.title)
        print self.driver.title
        self.driver.find_element_by_xpath("//div[@class = 'sidebar-nav navbar-collapse']/ul/li[3]/a").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Projects").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Edit").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Units").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Edit").click()
        time.sleep(2)
        self.driver.find_element_by_id("UnitName").clear()
        self.driver.find_element_by_id("UnitName").send_keys("Automation Test unit name")
        time.sleep(1)
        self.driver.find_element_by_id("Description").clear()
        self.driver.find_element_by_id("Description").send_keys("Automation Test Description Name")
        time.sleep(1)
        self.driver.find_element_by_id("Budget").clear()
        self.driver.find_element_by_id("Budget").send_keys("200000")
        time.sleep(1)
        self.driver.find_element_by_id("ContactName").clear()
        self.driver.find_element_by_id("ContactName").send_keys("Automation Test contact name")
        time.sleep(1)
        self.driver.find_element_by_id("ContactPhone").clear()
        self.driver.find_element_by_id("ContactPhone").send_keys("8897621322")
        time.sleep(1)
        self.driver.find_element_by_id("EmailId").clear()
        self.driver.find_element_by_id("EmailId").send_keys("unit_test@mailinator.com")
        time.sleep(1)
        self.driver.find_element_by_id("StartDate").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[6]/td[1]").click()
        time.sleep(2)

        self.driver.find_element_by_id("EndDate").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[4]/td[2]").click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//select[@id='assignedIA']/option[3]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='PaymentFoundationApprover']/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='PaymentIAApp']/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='state']/option[29]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='Dist']/option[11]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='subDist']/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='GP']/option[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='village']/option[2]").click()
        time.sleep(2)

        # self.driver.find_element_by_id("btnAddnewTag").click()
        # time.sleep(3)
        # self.driver.switch_to_active_element()
        # self.driver.find_element_by_id("tgName").send_keys("testtag2")
        # self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
        # time.sleep(3)
        # self.driver.switch_to_alert().accept()
        # self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[2]").click()
        tag = self.driver.find_element_by_xpath("//select[@id='availableTags']/option[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id("idAddTag").click()
        time.sleep(2)
        #addtag = self.driver.find_element_by_xpath("//*[contains(text(), 'Add')]")
        self.driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
        time.sleep(3)




        # **************** #
        # Logout validation #
        # **************** #
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/nav/ul/li[2]/a/i[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/nav/ul/li[2]/ul/li[4]/a").click()
        time.sleep(1)
        self.assertIn("SUNIDHI" , self.driver.title)
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
