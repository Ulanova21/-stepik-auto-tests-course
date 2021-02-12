from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def calc(number_1, number_2):
    return str((int(number_1) + int(number_2)))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
