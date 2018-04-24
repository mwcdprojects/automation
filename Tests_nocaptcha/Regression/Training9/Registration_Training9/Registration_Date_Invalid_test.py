#!C:\Python27\python.exe

"""
Testcase :Enter the registration date as < 1/1/2017 and submit the form
Expected Result: System should not allow to submit the form by throwing an error stating:
"Registration Date must not be less than January 1, 2017. Please enter the correct date"

"""
import sys
import unittest
from selenium import webdriver
import time
import string
import random
import verhoeff



class login(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
        self.a = string.ascii_letters + string.digits
        self.id1 = ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.id2 = ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.accountno = ''.join(random.choice(string.digits) for i in range(18))
        self.health_id = "H" + ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.aadhaar1 = verhoeff.VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        for i in range(20):
            if int(self.aadhaar1[0]) == 0:
                self.aadhaar1 = verhoeff.VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break
        self.aadhaar2 = verhoeff.VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        for i in range(20):
            if int(self.aadhaar2[0]) == 0:
                self.aadhaar2 = verhoeff.VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break
        self.driver = webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("test_automation123@mailinator.com")
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
        time.sleep(1)
        self.driver.find_element_by_id("btnNewbeneficiary").click()
        time.sleep(2)

        # Fill in all the valid details #

        self.driver.find_element_by_id("dpicker1").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[5]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[4]").click()
        time.sleep(1)
        print "Registration Date => ", self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute(
            "value")
        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(1)
        #print Aadhaar_avaialbilty_data[1].get_attribute('value')
        Aadhaar_avaialbilty_data[0].click()
        time.sleep(1)
        Aadhar_husband_availability = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        Aadhar_husband_availability[0].click()
        time.sleep(1)
        self.driver.find_element_by_id("txtNameAsInAadhar").send_keys("Shraddha H")
        time.sleep(1)
        print "Beneficiary Name is " , self.driver.find_element_by_id("txtNameAsInAadhar").get_attribute("value")
        self.driver.find_element_by_id("txtAadhar").send_keys(self.aadhaar1)
        time.sleep(1)
        print "Beneficiary ID is ", self.aadhaar1
        self.driver.find_element_by_xpath("//a[@id='BenAadhaarCheck']").click()
        time.sleep(2)

        self.driver.find_element_by_id("txtFNameAsInAadhaar").send_keys("Suhas H")
        time.sleep(1)
        self.driver.find_element_by_id("txtFAadhar").send_keys(self.aadhaar2)
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='HusbandAadhaarCheck']").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//label[@id='lblBenAadharStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblBenAadharStatus']").text , "Aadhaar is allowed for Registration")
        print self.driver.find_element_by_xpath("//label[@id='lblHusbandAadharStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblHusbandAadharStatus']").text, "Aadhaar is allowed for Registration")

        self.driver.find_element_by_xpath("//input[@id='Phone']").send_keys("9980776512")
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Category']/option[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='HealthId']").send_keys(self.health_id)
        self.driver.find_element_by_xpath("//input[@id='dpicker2']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[5]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[9]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[2]").click()
        time.sleep(1)
        print "Last Menstrual Period (LMP) Date => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker2']").get_attribute("value")
        self.driver.find_element_by_xpath("//input[@id='dpicker3']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[10]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[7]").click()
        time.sleep(1)
        print "Date of Reg of MCP card at AWC/ Subcenter => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker3']").get_attribute("value")

        self.driver.find_element_by_xpath("//input[@id='AddressLine1']").send_keys('786')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AddressLine2']").send_keys('87th Cross')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AddressLine3']").send_keys('Bull Temple Road')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AreaLocalitySector']").clear()
        self.driver.find_element_by_xpath("//input[@id='AreaLocalitySector']").send_keys('Alankady')
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='drpAnganvaadi']/option[4]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@id='Pincode']").send_keys('670645')
        time.sleep(1)
        self.driver.find_element_by_id("BankIFSCCode").send_keys("SBIN0005099")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='ifscButton1']").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//label[@id='lblStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblStatus']").text , "Valid IFSC Code")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='BankAccountNo']").send_keys(self.accountno)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='txtAccountHoldersName']").send_keys("Shraddha H")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='btnVerify']").click()
        time.sleep(5)
        self.driver.switch_to_active_element()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(5)
        self.driver.implicitly_wait(20)
        print self.driver.find_element_by_xpath("//span[@class='field-validation-error']").text
        self.assertTrue(self.driver.find_element_by_xpath("//span[@class='field-validation-error']").text, "Registration Date must not be less than January 1, 2017. Please enter the correct date")
        #self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/h5").text , " The beneficiary application form is sent for approval")


    def tearDown(self):
        if self.driver.title == "PRADHAN MANTRI MATRU VANDANA YOJANA":
            self.driver.quit()
        else:
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[@class='dropdown']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//a[@id='btnlogout']").click()
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
