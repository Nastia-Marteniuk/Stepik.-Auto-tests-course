from selenium import webdriver
import time
import math
import numpy

def calc(x):
  return str(numpy.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    ans = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(ans)

    button2 = browser.find_element_by_css_selector("button")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
