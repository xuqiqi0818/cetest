#coding=utf-8
import time 
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()  

driver.get("http://118.24.255.132:9090/shopxo")
driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/a/img').click() #这样虽然新开了一个网页但是不能定位到新网页

# 作用域切换到新开窗口
driver.switch_to_window(driver.window_handles[-1])
print(driver.window_handles)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button').click()
