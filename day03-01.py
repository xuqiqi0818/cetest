#coding=utf-8
import time 
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()  

driver.get("http://ctw.testgoup.com/html/login.html")

time.sleep(3)
driver.find_element_by_xpath('//*[@id="userLogin"]').click()

# 点击alert的确定按钮
driver.switch_to_alert().accept()
