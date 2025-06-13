import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search_product(driver):
    driver.get("https://www.amazon.com")
    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.send_keys("wireless mouse")
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    assert "mouse" in driver.title.lower()
    results = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-title span")
    assert results, "No results found"

    # Screenshot for report
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/search_results.png")
