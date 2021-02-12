from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .first_class .first")
    input1.send_keys("Ivan")
    time.sleep(3)
    input2 = browser.find_element_by_css_selector(".first_block .second_class .second")
    input2.send_keys("Petrov")
    time.sleep(3)
    input3 = browser.find_element_by_css_selector(".third_class .third")
    input3.send_keys("asdf@mail.ru")
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    time.sleep(10)
    browser.quit()
