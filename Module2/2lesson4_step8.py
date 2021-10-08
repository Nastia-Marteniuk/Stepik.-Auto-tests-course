from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import numpy

def calc(x):
  return str(numpy.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    ans = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(ans)

    button2 = browser.find_element_by_id("solve").click()

finally:
    time.sleep(30)
    browser.quit()
