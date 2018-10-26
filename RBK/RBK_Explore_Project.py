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

        self.driver.find_element_by_xpath("//div[@class='navbar-collapse']/ul/li/a").click()
        self.driver.find_element_by_id("freeSearch").send_keys("GLPS ERAVIPURAM")
        time.sleep(1)
        self.driver.find_element_by_id("btnFreeSearch").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//div[@class='col-md-12 card mt-1 no-padding home-project-card']/a/h4").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='col-md-12 card mt-1 no-padding home-project-card']/a/h4").text , "GLPS ERAVIPURAM")
        time.sleep(2)
        self.driver.find_elements_by_xpath("//select[@id='dist']/option")[6].click()
        time.sleep(2)
        #self.driver.find_elements_by_xpath("//select[@id='village']/option")[1].click()
        #time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='btn-group']/button/span").click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//select[@id='example-multiple-selected']/option")[0].click()
        self.driver.find_elements_by_xpath("//select[@id='example-multiple-selected']/option")[1].click()
        self.driver.find_elements_by_xpath("//select[@id='example-multiple-selected']/option")[2].click()
        time.sleep(2)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        self.driver.find_element_by_id("anc_1848").click()
        time.sleep(2)
        self.driver.find_element_by_id("anc_1848").click()
        time.sleep(2)

        #self.driver.find_element_by_id("DonationAmount1848").send_keys("100000")
        #time.sleep(2)
        #self.driver.find_element_by_link_text("DONATE").click()
        #time.sleep(2)
        #self.driver.find_element_by_link_text("VIEW DONATION BOX").click()
        #time.sleep(2)
        self.driver.find_element_by_id("DonationAmount1848").clear()
        self.driver.find_element_by_id("DonationAmount1848").send_keys("100000")
        time.sleep(2)
        self.driver.find_element_by_id("donatebutton1848").click()
        time.sleep(2)

        self.driver.find_element_by_link_text("PROCEED TO PAY").click()
        time.sleep(2)

        self.driver.find_element_by_id("name").send_keys("test test")
        self.driver.find_element_by_id("email").send_keys("archena@billionlives.in")
        self.driver.find_element_by_id("PhoneNumber").send_keys("4323212233")
        self.driver.find_elements_by_xpath("//div[@class='form-group']/select/option")[1].click()
        self.driver.find_element_by_id("whatsapp_agree").click()
        self.driver.find_element_by_id("cditsubmit").click()
        time.sleep(2)
        self.driver.find_element_by_id("donation_gateway_id").click()
        time.sleep(2)
        self.driver.find_element_by_id("gt_Submit").click()
        time.sleep(2)
        self.driver.quit()





    def tearDown(self):
        if self.driver.title == "Rebuild Kerala":
            self.driver.quit()
        else:
            pass
            #
            # time.sleep(3)
            # self.driver.find_element_by_xpath("//*[@id=\"main-menu\"]/div/ul[5]/li/a").click()
            # time.sleep(2)
            # self.driver.find_element_by_xpath("/html/body/nav[2]/div/div/div/ul[5]/li/ul/li[2]/a").click()
            # time.sleep(1)
            # self.assertIn("PRADHAN MANTRI MATRU VANDANA YOJANA", self.driver.title)
            # print self.driver.title
            # print "User Logged out Successfully"
            # self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print "fails", len(testResult.failures)
    if len(testResult.failures) > 0:
        sys.exit(1)
