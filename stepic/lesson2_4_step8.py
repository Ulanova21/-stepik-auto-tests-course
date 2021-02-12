import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)



    house_price = WebDriverWait(browser, 25).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button1 = browser.find_element_by_id("solve")
    button1.click()


finally:
    time.sleep(10)
    browser.quit()

