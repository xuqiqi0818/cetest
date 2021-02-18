# coding=utf-8
# bilibili绕过cookie
import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()

driver.get("https://www.bilibili.com/")

cookie = [{'domain': '.bilibili.com',  'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': '6224b52923bbedd0ded915c175764566'}, 
{'domain': '.bilibili.com',  'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': '9c424596%2C1621569835%2Ca2790*b1'},
 {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '376067334'},
  {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': 'cvrkcnps'},
          {'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 'secure': False, 'value': '-53268994'},
           {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': '32323A71-6B02-4A38-ABEB-CF6504AD9DAF143086infoc'}, 
           {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '35ef735f45ccb7cc'}, 
           {'domain': '.bilibili.com',  'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '15C1E075-743D-F119-6710-61A6772D0B2F03226infoc'}]
# time.sleep(30)
# print(driver.get_cookies())
driver.delete_all_cookies()
for i in cookie:
    driver.add_cookie(i)

driver.refresh()
