import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def ans():
	return str(math.log(int(time.time())))

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_different_links(link, browser):
	browser.get(link)
	
	input1 = browser.find_element_by_css_selector("textarea")
	textForInput = ans()
	input1.send_keys(textForInput)

	button1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
	button1.click()

	time.sleep(3)

	feedback = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text

	assert "Correct!" == feedback
