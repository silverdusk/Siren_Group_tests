import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pytest_html import html


@pytest.fixture
def driver():
    # Set up the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    # Quit the driver after the test
    driver.quit()


def test_siren_website(driver):
    # Open the website
    driver.get("https://hb-eta.stage.sirenltd.dev/siding")

    # Find and click the "Get estimate" button
    get_estimate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Get estimate')]")
    get_estimate_button.click()

