#coding=utf-8
import time 
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()  

driver.get("http://118.24.255.132:9090/shopxo/admin.php")

username = ('name','username')
password = ('name','login_pwd')
btn = ('xpath','/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
index = ('xpath','//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
find_element(driver,username).send_keys('admin')
find_element(driver,password).send_keys('shopxo')
find_element(driver,btn).click()
e = find_element(driver,index)
assert e.text == '首页'
# driver.find_element_by_name('username').send_keys('admin')
# driver.find_element_by_name('login_pwd').send_keys('shopxo')
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
# driver.implicitly_wait(5)

# e = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
# assert e.text == '首页'
print('通过')
