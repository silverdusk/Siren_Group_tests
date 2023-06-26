import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# from pytest_html import html


@pytest.fixture
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
    yield driver
    # Teardown - quit the WebDriver after the test completes
    driver.quit()


def test_siren_website(driver):
    # Step 1: Open the website and check the title
    driver.get("https://hb-eta.stage.sirenltd.dev/siding")
    # print(driver.title)
    assert "Siding - HomeBuddy" in driver.title

    # Step 2: Find the zip code input field and enter a valid zip code
    zip_code_input = driver.find_element(By.ID, "zipCode")
    zip_code_input.send_keys("09090")

    # Step 3: Find and click the "Get estimate" button
    get_estimate_button = driver.find_element(By.CLASS_NAME, "customButton")
    get_estimate_button.click()

    # Step 4: Wait and check the page title of the next page
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What type of project is this?')]")))

    # Step 5: Check that "Next" button disabled until the type is selected
    # project_type1_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]")
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 6: Select the type and click "Next"
    # wait = WebDriverWait(driver, 10)
    # project_type1_radio = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='sdProjectType'][value='1']")))
    project_type1_radio = driver.find_element(By.CSS_SELECTOR, "input[name='sdProjectType'][value='1']")
    # project_type1_radio.click()
    driver.execute_script("arguments[0].click();", project_type1_radio)

    assert next_button.is_enabled()
    next_button.click()

    # Step 7: Wait and check the page title of the next page
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What kind of siding do you want?')]")))

    # Step 8: Check that "Next" button disabled until the type is selected
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 9: Select the type and click "Next"
    siding_kind1_radio = driver.find_element(By.CSS_SELECTOR, "input[name='sdKind'][value='1']")
    driver.execute_script("arguments[0].click();", siding_kind1_radio)
    assert next_button.is_enabled()
    next_button.click()
