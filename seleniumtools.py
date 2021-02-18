"""
    显式等待：固定的用法，知道怎么用就行了
"""
# 类
from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator, timeout=60):
    """
        方法：显式等待，动态查找元素
        参数：
            driver：浏览器的句柄/把柄
            locator：
                - ("id", "username")
                - ("xpath", "xxxxxxx")
                - ("name", "xxxxxx")
                - ("css selector", "xxxxx")
                - ("class name", "xxxxxxxx")
                - ("link text", "抗击肺炎")
                - ("partial link text", "抗击肺")
            timeout：超时时间

        返回值：找到元素，就直接返回，没有找到就报错
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))