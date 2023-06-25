import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    # Set up the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    # Quit the driver after the test
    driver.quit()