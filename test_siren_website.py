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

    # Step 4: Wait and check the page title "Project type"
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What type of project is this?')]")))

    # Step 5: Check that "Next" button disabled until the type is selected
    # project_type1_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]")
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 6: Select the type and click "Next"
    project_type1_radio = driver.find_element(By.CSS_SELECTOR, "input[name='sdProjectType'][value='1']")
    driver.execute_script("arguments[0].click();", project_type1_radio)

    assert next_button.is_enabled()
    next_button.click()

    # Step 7: Wait and check the page title "What kind of siding do you want?"
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What kind of siding do you want?')]")))

    # Step 8: Check that "Next" button disabled until the type is selected
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 9: Select the type and click "Next"
    siding_kind1_radio = driver.find_element(By.XPATH, "(//div[@class='kindOfSiding__item'])[1]")
    siding_kind1_radio.click()
    assert next_button.is_enabled()
    next_button.click()

    # Step 10: Wait and check the page title "Approximately how many square feet will be covered with new siding?"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'Approximately how many square feet will be covered')]")))

    # Step 11: Input the area value and click "Next"
    siding_area_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.ID, "squareFeet")))
    siding_area_input.clear()
    siding_area_input.send_keys("42")
    next_button = driver.find_element(By.XPATH, "//button[@data-autotest-button-submit-next]")
    next_button.click()

    # Step 12: Wait and check the page title "Amount of stories"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'How many stories is your house?')]")))
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 13: Select the amount of stories and click "Next"
    stories_amount2_radio = driver.find_element(By.CSS_SELECTOR, "input[name='sdStories'][value='2']")
    # stories_amount2_radio.click()
    driver.execute_script("arguments[0].click();", stories_amount2_radio)
    assert next_button.is_enabled()
    next_button.click()

    # Step 14: Wait and check the page title of the next page "Homeowner authorization"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'Are you the homeowner or authorized to make property changes?')]")))
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 15: Select the amount of stories and click "Next"
    internal_owner_yes_radio = driver.find_element(By.CSS_SELECTOR, "input[name='internalOwner'][value='1']")
    # stories_amount2_radio.click()
    driver.execute_script("arguments[0].click();", internal_owner_yes_radio)
    assert next_button.is_enabled()
    next_button.click()

    # Step 16: Wait and check the page title of the next page "Who should I prepare this estimate for?"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'Who should I prepare this estimate for?')]")))

    # Step 17: Fill the form and click "Next"
    
    # 17.1 Find and fill the "Full name" input field
    full_name_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "fullName")))
    full_name_input.clear()
    name = "John"
    family_name = "Doe" 
    full_name_input.send_keys(name + " " + family_name)

    # 17.2 Find and fill the "Email address" input field
    email_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "email")))
    email_input.clear()
    email_input.send_keys("test@test.test")

    # 17.4 Click the "Next" button
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    next_button.click()

    # Step 18: Wait and check the page title of the next page "Who should I prepare this estimate for?"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'Who should I prepare this estimate for?')]")))
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")