#!/usr/bin/env python3

from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe')
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('найден элемент <%s> с данным именем класса' % (elem.tag_name))
except:
    print('не удалось найти элемент с данным именем класса')




