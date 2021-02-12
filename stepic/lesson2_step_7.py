from selenium import webdriver
import time
import math

from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    pic_element = browser.find_element_by_id("treasure")
    valuex_element = pic_element.get_attribute("valuex")
    x = valuex_element

    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    option3 = browser.find_element_by_class_name("btn-default")
    option3.click()


finally:
    time.sleep(5)
    browser.quit()
    print(x)