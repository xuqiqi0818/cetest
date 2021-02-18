#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()  

driver.get("http://www.baidu.com/")
# <input id="kw" name="wd" class="s_ipt" value="彻底卸载谷歌浏览器" maxlength="255" autocomplete="off">
# id
driver.find_element_by_id('kw').send_keys('hello!')

# xpath
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('nihao')


# 一部分文字定位超链接
# driver.find_element_by_link_text('地图').click()

# driver.find_element_by_partial_link_text('地').click()
driver.find_element_by_id('su').click()

driver.quit()
