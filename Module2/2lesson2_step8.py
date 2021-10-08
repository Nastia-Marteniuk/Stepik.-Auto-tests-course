from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Opa")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Opa")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("Opa@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'FileOpa.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button1 = browser.find_element_by_css_selector("button")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
