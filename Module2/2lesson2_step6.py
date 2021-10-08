from selenium import webdriver
from selenium.webdriver.support.ui import Select
import numpy
import time
import math

def calc(x):
  return str(numpy.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    ans = calc(x)

    browser.execute_script("window.scrollBy(0, 200);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(ans)

    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    radiobutton1 = browser.find_element_by_id("robotsRule")
    radiobutton1.click()

    button1 = browser.find_element_by_css_selector("button")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
