#coding=utf-8
import time 
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()  

driver.get("http://118.24.255.132:9090/shopxo/admin.php")
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('login_pwd').send_keys('shopxo')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
driver.implicitly_wait(5)

# 作用域由大网页切换到小网页中
iframe = driver.find_element_by_id('ifcontent')
driver.switch_to_frame(iframe)

e = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
print(e.text)

driver.switch_to_default_content()
e = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
assert e.text == '首页'
print('通过')