from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    ans = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(ans)

    button1 = browser.find_element_by_css_selector("button")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
