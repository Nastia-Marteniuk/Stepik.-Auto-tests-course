from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_an_add_to_cart_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button[type='submit']")
    assert button, "No such button"
