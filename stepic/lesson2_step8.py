from selenium import webdriver
import time
import os

from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ghj123@mail.ru")

    button = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "hello.txt")

    button.send_keys(file_path)

    button1 = browser.find_element_by_class_name("btn")
    button1.click()


finally:
    time.sleep(5)
    browser.quit()

