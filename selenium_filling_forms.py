#!/usr/bin/env python
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_id("identifierId").send_keys('ihorvturchyn@gmail.com')
time.sleep(3)
driver.find_element_by_id("identifierNext").click()
#time.sleep(5)

# driver.find_element_by_name("password").send_keys('VerizonR523')
# driver.find_element_by_id("passwordNext").click()
# time.sleep(5)

