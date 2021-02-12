from selenium import webdriver
import time
import math
from selenium.webdriver.chrome.options import Options


options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    time.sleep(4)

    button = browser.find_element_by_class_name("trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button1 = browser.find_element_by_class_name("btn")
    button1.click()

finally:
    time.sleep(5)
    browser.quit()


