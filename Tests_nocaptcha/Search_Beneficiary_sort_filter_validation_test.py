#!C:\Python27\python.exe
import sys
import collections
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

    def print_beneficiary_details(self):
        print "Beneficiary Name is ", self.driver.find_element_by_id("NameAsInAadhar").get_attribute('value')
        print "Beneficiary Aadhaar Number is ", self.driver.find_element_by_id("AadharNo").get_attribute('value')
        print "Beneficiary Alternate Number is ", self.driver.find_element_by_id(
            "BeneficiaryAlternatenumber").get_attribute('value')
        print "Beneficairy Contact Number is ", self.driver.find_element_by_id("Phone").get_attribute('value')
        print "Beneficiary Husband Name is ", self.driver.find_element_by_id("FNameAsInAadhar").get_attribute('value')
        print "Field functionary is ", self.driver.find_element_by_id("Anganvaadi").get_attribute('value')
        print "Village is ", self.driver.find_element_by_id("VillageName").get_attribute('value')
        print "Block is ", self.driver.find_element_by_id("Block").get_attribute('value')
        print "District ", self.driver.find_element_by_id("District").get_attribute('value')
        print "State ", self.driver.find_element_by_id("State").get_attribute('value')
        print "Details Entered by ", self.driver.find_element_by_id("EnteredbyUser").get_attribute('value')
        print "Details Verified by ", self.driver.find_element_by_id("VerifiedbyUser").get_attribute('value')
        print "Bank is ", self.driver.find_element_by_id("BankName").get_attribute('value')
        print "Bank Account number is ", self.driver.find_element_by_id("BankAccountNo").get_attribute('value')
    """
    def test_01_Search_Beneficiary_sort(self):
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
       
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        # *********************************** #
        # Search Beneficiary validation       #
        # Search By Field Functionary number  #
        # Sort field validation ************* #
        # *********************************** #

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("ID").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Ids = []
        for each in table_data:
            Ids.append(each.text.split(" ")[0])
        if compare(Ids , sorted(Ids)):
            print 'Ids are sorted in ascending order'
        print "Sorted in ascending order" , self.driver.find_element_by_xpath("//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("ID").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Ids = []
        for each in table_data:
            Ids.append(each.text.split(" ")[0])
        if compare(Ids, sorted(Ids,reverse=True)):
            print 'Ids are sorted in descending order'
        print "Sorted in descending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("ID Type").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Idtype = []
        for each in table_data:
            Idtype.append(each.text.split(" ")[1])
        if compare(Idtype, sorted(Idtype)):
            print 'Id Type data is sorted in ascending order'
        print "Sorted in ascending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("ID Type").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Idtype = []
        for each in table_data:
            Idtype.append(each.text.split(" ")[1])
        if compare(Idtype, sorted(Idtype, reverse=True)):
            print 'Id Type data is sorted in descending order'
        print "Sorted in descending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("Mobile Number").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Mobile = []
        for each in table_data:
            Mobile.append(each.text.split(" ")[2])
        if compare(Mobile, sorted(Mobile)):
            print 'Mobile Numbers are sorted in ascending order'
        print "Sorted in ascending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("Mobile Number").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Mobile = []
        for each in table_data:
            Mobile.append(each.text.split(" ")[2])
        if compare(Mobile, sorted(Mobile, reverse=True)):
            print 'Mobile Numbers are sorted in descending order'
        print "Sorted in descending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("Beneficiary Name").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Bname = []
        for each in table_data:
            Bname.append(each.text.split(" ")[3])
        if compare(Bname, sorted(Bname)):
            print 'Beneficiary Names are sorted in ascending order'
        print "Sorted in ascending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)
        self.driver.find_element_by_link_text("Beneficiary Name").click()
        time.sleep(1)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Bname = []
        for each in table_data:
            Bname.append(each.text.split(" ")[3])
        if compare(Bname, sorted(Bname, reverse=True)):
            print 'Beneficiary Names are sorted in descending order'
        print "Sorted in descending order", self.driver.find_element_by_xpath(
            "//span[@class='grid-sort-arrow']").is_displayed()
        time.sleep(1)

        # *********************************** #
        # Search Beneficiary validation       #
        # Search By Field Functionary number  #
        # Filter field validation *********** #
        # *********************************** #
    def test_02_Search_Beneficiary_filter_ID(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd1")
        print "Password entered"
        time.sleep(3)
        
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        # Valdiate ID sortfilter - Equals value

        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[1]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[1]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("752752")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("752752").click()
        time.sleep(3)
        self.print_beneficiary_details()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate ID sortfilter - Contains value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[1]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[2]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("75")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("752752").click()
        time.sleep(3)
        self.print_beneficiary_details()

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate ID sortfilter - Startswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[1]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[3]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("75")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("752752").click()
        time.sleep(3)
        self.print_beneficiary_details()

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate ID sortfilter - Endswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[1]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[4]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("52")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("752752").click()
        time.sleep(3)
        self.print_beneficiary_details()
    """
    def test_03_Search_Beneficiary_filter_IDType(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd1")
        print "Password entered"
        time.sleep(3)

        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate IDtype sortfilter - Equals value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[2]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[1]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("Passport")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        bodyText = self.driver.find_element_by_tag_name('body').text
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Idtypedata = []
        print "table data for IDTypefilter" , table_data
        for each in table_data:
            Idtypedata.append(each.text.split(" ")[1])
        print "IDType data" , Idtypedata
        if set(Idtypedata) == set(["Passport"]):
            print 'Data filtered with Passport as ID Type'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate IDType sortfilter - Contains value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[2]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[2]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("Aad")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        print "Table_data 2" , table_data
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Idtypedata = []
        for each in table_data:
            Idtypedata.append(each.text.split(" ")[1])
        print "Idtypedata" , Idtypedata
        if set(Idtypedata) == set(["Aadhaar"]):
            print 'Data filtered with Aadhaar containing Aa string in ID Type'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate IDType sortfilter - Startswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[2]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[3]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("Aa")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Idtypedata = []
        for each in table_data:
            Idtypedata.append(each.text.split(" ")[1])
        if set(Idtypedata) == set(["Aadhaar"]):
            print 'Data filtered with Aadhaar that starts with Aa in ID Type'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate IDType sortfilter - Endswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[2]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[4]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("ar")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Idtypedata = []
        for each in table_data:
            Idtypedata.append(each.text.split(" ")[1])
        if set(Idtypedata) == set(["Aadhaar"]):
            print 'Data filtered with Aadhaar that ends with ar in ID Type'
        time.sleep(1)
    
    def test_04_Search_Beneficiary_filter_MobileNumber(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd1")
        print "Password entered"
        time.sleep(3)

        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Mobile Number sortfilter - Equals value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[3]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[1]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("9876543212")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Numbers = []
        for each in table_data:
            Numbers.append(each.text.split(" ")[2])
        if "9876543212" in Numbers:
            print 'Data filtered with Number 9876543212 Mobile Number field.'
        time.sleep(1)
        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Mobile Number sortfilter - Contains value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[3]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[2]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("432")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Numbers = []
        for each in table_data:
            Numbers.append(each.text.split(" ")[2])
        if "9876543212" in Numbers:
            print 'Data filtered with 432 Number in Mobile Number field.'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Mobile number sortfilter - Startswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[3]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[3]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("987")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Numbers = []
        for each in table_data:
            Numbers.append(each.text.split(" ")[2])
        print "Numbers" , Numbers
        if "9876543212" in Numbers:
            print 'Data filtered starting with 987 in Mobile Number field.'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Mobile Number sortfilter - Endswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[3]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[4]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("212")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Numbers = []
        for each in table_data:
            Numbers.append(each.text.split(" ")[2])
        if "9876543212" in Numbers:
            print 'Data filtered ending with 212 in Mobile Number field.'
        time.sleep(1)

    def test_05_Search_Beneficiary_filter_BeneficiaryName(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://mwcd1.fundright.in/BackOffice/useraccount/login")
        time.sleep(3)
        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation12@example.com")
        time.sleep(3)
        print "Email entered"
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd1")
        print "Password entered"
        time.sleep(3)

        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print self.driver.title

        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Beneficiary Name sortfilter - Equals value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[4]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[1]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("Mehak")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Names = []
        print "Table_data" , table_data
        for each in table_data:
            print each.text
            Names.append(each.text.split(" ")[-1])
        print "Names" , Names
        if "Mehak" in Names:
            print 'Data filtered with name Mehak in Beneficiary Name field.'
        time.sleep(1)
        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Beneficiary Name sortfilter - Contains value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[4]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[2]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("hak")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Names = []
        for each in table_data:
            Names.append(each.text.split(" ")[-1])
        if "Mehak" in Names:
            print 'Data filtered with hak string in Beneficiary Name field.'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Beneficiary Name sortfilter - Startswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[4]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[3]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("Me")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Names = []
        for each in table_data:
            Names.append(each.text.split(" ")[-1])
        if "Mehak" in Names:
            print 'Data filtered with starting characters Me in Beneficiary Name field.'
        time.sleep(1)

        self.driver.get("http://mwcd1.fundright.in/BackOffice/Beneficiary/BeneficiaryList")
        self.driver.find_element_by_xpath("//li[@class='dropdown']/a").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Search Beneficiary").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@id='Anganvaadi']/option[6]").click()
        time.sleep(1)
        self.driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        # Valdiate Beneficiary Name sortfilter - Endswith value

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div/div/table/thead/tr/th[4]/div[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//select[@class='grid-filter-type form-control']/option[4]").click()
        self.driver.find_element_by_xpath("//input[@class='grid-filter-input form-control']").send_keys("hak")
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary grid-apply']").click()
        time.sleep(2)
        table_data = self.driver.find_elements_by_xpath(".//tr[@class='grid-row ']")
        tables_dict = {}
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        Names = []
        print table_data
        for each in table_data:
            Names.append(each.text.split(" ")[-1])
        if "Mehak" in Names:
            print 'Data filtered with ending characters hak in Beneficiary Name field.'
        time.sleep(1)


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
