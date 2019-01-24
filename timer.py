from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("C:\\Users\\arche\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.worldtimebuddy.com/")
wait = WebDriverWait(driver, 10)

# **************** #
# Login validation #
# **************** #

driver.find_element_by_id('tab_signin').click()
#driver.find_element_by_xpath('//*[@id="tabs-func"]/li[1]/div/a[3]').click()
driver.find_element_by_link_text("Email / Password").click()
time.sleep(4)
#wait = WebDriverWait(driver, 20)
##Enter email
driver.find_element_by_name('email').click()
driver.find_element_by_name('email').send_keys('rarthee@gmail.com')

##Enter password
driver.find_element_by_name('password').click()
driver.find_element_by_name('password').send_keys('sahana')

##Click submit

driver.find_element_by_name('submit').click()
#wait = WebDriverWait(driver, 10)
time.sleep(4)
#assert "Contentional Login - World Time Buddy" in driver.title
assert driver.title == 'Time Converter and World Clock - Conversion at a Glance - Pick best time to schedule conference calls, webinars, online meetings and phone calls.'

# **************** #
# Time changes for #
# current day      #
# **************** #

#current1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'toolbar-default')))
#current1.click()
#print('current day')

# **************** #
# Time changes for #
# a later day      #
# **************** #

#laterday1 = WebDriverWait(driver, 10).\
#    until(EC.presence_of_elements_located\
#                     ((By.CLASS_NAME,'date-jump-txt')))
#laterday1[1].click()
#print('later day')


# **************** #
# Remove a country #
# **************** #
time.sleep(1)

close1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'close')))
close1.click()
print('close')
#close=driver.find_elements_by_xpath('//*[@id="locations"]/div[3]/div[5]/div[1]/div/a[1]')

# **************** #
# Add a country    #
# **************** #
#driver.find_element_by_xpath('//*[@id="location"]').click()
add1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'location')))
add1.click()
add1.sendkeys('Japan')
print('add')


# **************** #
# Click Features   #
# **************** #
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'tab_features')))
element.click()
print('features')
##Go back to previous page

driver.execute_script("window.history.go(-1)")

# **************** #
# Click World clock#
# Widget           #
# **************** #
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'tab_widgets')))
element.click()
driver.find_element_by_xpath('//*[@id="tabs-nav"]/li[2]/div/a[2]').click()
driver.execute_script("window.history.go(-1)")
print('Widget')
# **************** #
#Click Sort Buttons#
# **************** #

##up
driver.find_element_by_xpath('//*[@id="sorter"]/a[1]').click()
print('sort up')
##down

driver.find_element_by_xpath('//*[@id="sorter"]/a[2]').click()

print('sort down')

# **************** #
#Switch to 12HR    #
# **************** #

driver.find_element_by_xpath('//*[@id="stAM"]').click()
print('12 hour')
# **************** #
#Switch to 12HR    #
# **************** #
driver.find_element_by_xpath('//*[@id="st24"]').click()
print('24 hour')