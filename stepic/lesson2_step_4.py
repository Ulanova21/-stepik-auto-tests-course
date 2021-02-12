from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    option3 = browser.find_element_by_class_name("btn")
    option3.click()


finally:
    time.sleep(5)
    browser.quit()
