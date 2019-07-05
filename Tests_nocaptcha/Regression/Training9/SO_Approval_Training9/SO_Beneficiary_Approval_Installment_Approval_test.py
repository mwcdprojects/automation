#!C:\Python27\python.exe

"""
Testcase :Beneficiary form will get approved and will be sent for UIDAI verification
 if Aadhaar is provided and then to the PFMS verification (bank details)
 test_01 :Register a beneficiary with valid Aadhaar card. Register for all three Instalments.
 test_02_FirstInstalment:  Approval of First Instalment by SO Officer.
 test_03_Second_Instalment: Approval of Second Instalment by SO Officer.
 test_04_Third_Instalment: Approval of Third Instalment by SO Officer.

"""
import sys
import collections
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
                print "Aadhaar1", self.aadhaar1
            else:
                break
        self.aadhaar2 = verhoeff.VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        for i in range(20):
            if int(self.aadhaar2[0]) == 0:
                self.aadhaar2 = verhoeff.VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
                print "Aadhaar2", self.aadhaar2
            else:
                break
        self.driver = webdriver.Chrome("C:\\Users\\arche\\chromedriver_win32\\chromedriver.exe")



    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation123@mailinator.com")
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
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[6]").click()
        time.sleep(1)
        print "Registration Date => ", self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute(
            "value")
        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(1)
        # print Aadhaar_avaialbilty_data[1].get_attribute('value')
        Aadhaar_avaialbilty_data[0].click()
        time.sleep(1)
        Aadhar_husband_availability = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        Aadhar_husband_availability[0].click()
        time.sleep(1)
        self.driver.find_element_by_id("txtNameAsInAadhar").send_keys("girijaaaa")
        time.sleep(1)
        print "Beneficiary Name is ", self.driver.find_element_by_id("txtNameAsInAadhar").get_attribute("value")
        self.driver.find_element_by_id("txtAadhar").send_keys(self.aadhaar1)
        time.sleep(1)
        print "Beneficiary ID is ", self.aadhaar1
        self.driver.find_element_by_xpath("//a[@id='BenAadhaarCheck']").click()
        time.sleep(2)

        self.driver.find_element_by_id("txtFNameAsInAadhaar").send_keys("Shyamm")
        time.sleep(1)
        self.driver.find_element_by_id("txtFAadhar").send_keys(self.aadhaar2)
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='HusbandAadhaarCheck']").click()
        time.sleep(2)
        print self.driver.find_element_by_xpath("//label[@id='lblBenAadharStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblBenAadharStatus']").text,
                        "Aadhaar is allowed for Registration")
        print self.driver.find_element_by_xpath("//label[@id='lblHusbandAadharStatus']").text
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblHusbandAadharStatus']").text,
                        "Aadhaar is allowed for Registration")

        self.driver.find_element_by_xpath("//input[@id='Phone']").send_keys("9990000016")
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Category']/option[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='HealthId']").send_keys(self.health_id)
        self.driver.find_element_by_xpath("//input[@id='dpicker2']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[3]").click()
        time.sleep(1)
        print "Last Menstrual Period (LMP) Date => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker2']").get_attribute("value")
        self.driver.find_element_by_xpath("//input[@id='dpicker3']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[6]").click()
        time.sleep(1)
        print "Date of Reg of MCP card at AWC/ Subcenter => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker3']").get_attribute("value")
        self.driver.find_element_by_xpath("//input[@id='AddressLine1']").send_keys('110')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='AddressLine2']").send_keys('2nd Main')
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
        self.assertTrue(self.driver.find_element_by_xpath("//label[@id='lblStatus']").text, "Valid IFSC Code")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='BankAccountNo']").send_keys(self.accountno)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='txtAccountHoldersName']").send_keys("girijaaaa")
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
        print self.driver.find_element_by_xpath("//div[@class='col-md-12']/h5").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='col-md-12']/h5").text , " The beneficiary application form is sent for approval")
        installments = self.driver.find_elements_by_xpath("//div[@class='col-md-12']/a")
        installments[1].click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='dpicker']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[8]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[3]").click()
        time.sleep(1)
        print "Date of Claim at the Field Functionary Centre => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker']").get_attribute("value")
        self.driver.find_element_by_xpath("//input[@id='dpicker1']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[5]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[2]").click()
        time.sleep(1)
        print "ANC Date => ", self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute("value")
        self.driver.find_element_by_xpath("//input[@id='btnSave']").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        print self.driver.find_element_by_xpath("//div[@class='md-col-12']/p[2]").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='md-col-12']/p[2]").text , "Second Instalment Saved Successfully")
        time.sleep(2)
        installments = self.driver.find_elements_by_xpath("//div[@class='col-md-12']/a")
        time.sleep(2)
        installments[2].click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='dpicker']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[5]").click()
        time.sleep(1)
        print "Date of Claim at the Field Functionary Centre => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker']").get_attribute("value")
        self.driver.find_element_by_xpath("//input[@id='dpicker1']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[10]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[3]").click()
        time.sleep(1)
        print "Date of Child Birth => ", self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute("value")
        self.driver.find_elements_by_xpath("//input[@id='GovtInstituteValue']")[0].click()
        time.sleep(1)
        self.driver.find_element_by_id("DeliveryInstitute").send_keys("Asha Health Care")
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='drpNoofChildren']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='maleId0']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='dpicker2']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']/option[7]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']/option[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td[7]").click()
        time.sleep(1)
        print "Date of completion of all vaccinations  => ", self.driver.find_element_by_xpath("//input[@id='dpicker2']").get_attribute(
            "value")
        self.driver.find_element_by_xpath("//input[@id='btnSave']").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(3)
        print self.driver.find_element_by_xpath("//div[@class='md-col-12']/p[2]").text
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='md-col-12']/p[2]").text,
                        "Third Instalment Saved Successfully")

    def test_02_FirstInstalment(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("test_automation_so1@mailinator.com")
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
        time.sleep(3)

        # Beneficiary Approval

        self.driver.find_element_by_partial_link_text("BENEFICIARY APPROVAL").click()
        time.sleep(2)
        #print self.driver.find_element_by_partial_link_text("BENEFICIARY APPROVAL")
        #print self.driver.find_element_by_xpath("//div[@class='tab-content']")
        #print self.driver.find_element_by_id("Beneficiary")
        frame = self.driver.find_element_by_xpath("//iframe[@id='approvalQueueGrid']")
        self.driver.switch_to_frame(frame)
        self.driver.find_elements_by_xpath("//span[@class='grid-filter-btn']")[1].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("girijaaaa")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='btn btn-info approve-btns']").click()
        self.driver.switch_to_active_element()
        time.sleep(1)
        buttons = self.driver.find_elements_by_xpath("//div[@class='ui-dialog-buttonset']/button")
        print len(buttons)
        for each in buttons:
            print each.text
        buttons[1].click()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)

    def test_03_SecondInstallmet(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("test_automation_so1@mailinator.com")
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
        time.sleep(3)

        # Beneficiary Approval

        self.driver.find_element_by_partial_link_text("INSTALMENT APPROVAL").click()
        time.sleep(2)
        #print self.driver.find_element_by_partial_link_text("BENEFICIARY APPROVAL")
        #print self.driver.find_element_by_xpath("//div[@class='tab-content']")
        #print self.driver.find_element_by_id("Beneficiary")
        frame = self.driver.find_element_by_xpath("//iframe[@id='approvalQueueGrid1']")
        self.driver.switch_to_frame(frame)
        self.driver.find_elements_by_xpath("//span[@class='grid-filter-btn']")[1].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("girijaaaa")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        print len(self.driver.find_elements_by_xpath("//a[@class='btn btn-info approve-btns']"))
        self.driver.find_elements_by_xpath("//a[@class='btn btn-info approve-btns']")[1].click()
        self.driver.switch_to_active_element()
        time.sleep(1)
        buttons = self.driver.find_elements_by_xpath("//div[@class='ui-dialog-buttonset']/button")
        print len(buttons)
        for each in buttons:
            print each.text
        buttons[1].click()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)

    def test_04_ThirdInstallmet(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("test_automation_so1@mailinator.com")
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
        time.sleep(3)

        # Beneficiary Approval

        self.driver.find_element_by_partial_link_text("INSTALMENT APPROVAL").click()
        time.sleep(2)
        #print self.driver.find_element_by_partial_link_text("BENEFICIARY APPROVAL")
        #print self.driver.find_element_by_xpath("//div[@class='tab-content']")
        #print self.driver.find_element_by_id("Beneficiary")
        frame = self.driver.find_element_by_xpath("//iframe[@id='approvalQueueGrid1']")
        self.driver.switch_to_frame(frame)
        self.driver.find_elements_by_xpath("//span[@class='grid-filter-btn']")[1].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("girijaaaa")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='btn btn-info approve-btns']").click()
        self.driver.switch_to_active_element()
        time.sleep(1)
        buttons = self.driver.find_elements_by_xpath("//div[@class='ui-dialog-buttonset']/button")
        print len(buttons)
        for each in buttons:
            print each.text
        buttons[1].click()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        print self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        time.sleep(2)


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