import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import string
from helper import *


@pytest.fixture
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
    yield driver
    # Teardown - quit the WebDriver after the test complete
    driver.quit()


def test_siren_website(driver):
    # Step 1: Open the website and check the title
    driver.get("https://hb-eta.stage.sirenltd.dev/siding")
    # print(driver.title)
    assert "Siding - HomeBuddy" in driver.title

    # Step 2: Find the zip code input field and enter a valid zip code
    zip_code_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-0]")
    zip_code_input.send_keys("09090")

    # Step 3: Find and click the "Get estimate" button
    get_estimate_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-0]")
    get_estimate_button.click()

    # Step 4: Wait and check the page title "Project type"
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What type of project is this?')]")))

    # Step 5: Check that "Next" button disabled until the type is selected
    # project_type1_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]")
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 6: Select the type and click "Next"
    project_type1_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]")
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
    siding_area_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-squarefeet-tel]")
    siding_area_input.clear()
    siding_area_input.send_keys("42")
    next_button = driver.find_element(By.XPATH, "//button[@data-autotest-button-submit-next]")
    next_button.click()

    # Step 12: Wait and check the page title "Amount of stories", check the "Next" button
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

    # Step 15: Select type of owner and click "Next"
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
    full_name_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-fullname-text]")
    full_name_input.clear()
    name = "John"
    family_name = "Doe" 
    full_name_input.send_keys(name + " " + family_name)

    # 17.2 Find and fill the "Email address" input field
    email_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-email-email]")
    email_input.clear()
    email_input.send_keys("test@test.test")

    # 17.4 Click the "Next" button
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    next_button.click()

    # Step 18: Wait and check the page title of the next page "What is your phone number?"
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'What is your phone number?')]")))

    # Step 19 Find and fill the "Phone number" field
    phone_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-phonenumber-tel]")
    phone_input.clear()
    phone_input.send_keys("2345678901")

    # Step 20 Find and click the "Submit my request" button
    submit_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-submit-my-request]")
    submit_button.click()

    # Step 21.1 If a number already exists in the system, input another number
    if element_exist_xpath(driver, "//h4[contains(text(),'This phone number and email already exist in our database')]"):

        # Find the phone input
        phone_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-phonenumber-tel]")

        # # Clear the phone value:

        # TODO: find out why options are not working here.
        # driver.execute_script("arguments[0].value = '';", phone_input)
        # phone_input.send_keys(Keys.CONTROL + "a")  # Select all text
        # phone_input.clear()

        # I use the "Backspace" because basic "clear()" func and even "CONTROL + a" are not working here
        phone_input.send_keys(10 * Keys.BACKSPACE)  # Delete selected text

        # Generate a new random phone number
        random_phone = random.choice('234567890') + ''.join(random.choices(string.digits, k=9))
        print("Random phone: " + random_phone)

        phone_input.send_keys(random_phone)
        # phone_input.send_keys("0051803490")

        # Find and click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
        next_button.click()

    # Step 21.2 Confirm the phone number
    if element_exist_xpath(driver, "//h4[contains(text(),'Please confirm your phone number.')]"):
        confirm_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-phone-number-is-correct]")
        confirm_button.click()

    # Step 22 Final Page
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'Thank you')]")))

    # Find the message element
    message_element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'Thank you')]")))

    # Get the text of the message element
    message_text = message_element.text

    # Extract the name from the message

    # Assuming the name is always preceded by "Thank you " and followed by ","
    start_index = len("Thank you ")
    end_index = message_text.index(",")
    actual_name = message_text[start_index:end_index].strip()

    # Compare the actual name with the expected name using an assertion
    assert actual_name == name, f"Expected name: {name}, Actual name: {actual_name}"


# Test_002 Check that we are showing the specific page for an unsupported zip code
def test_zip_code_unsupported(driver):
    # Step 1: Open the website and check the title
    driver.get("https://hb-eta.stage.sirenltd.dev/siding")
    assert "Siding - HomeBuddy" in driver.title

    # Step 2: Find the zip code input field and enter a valid but not supported zip code
    zip_code_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-0]")
    zip_code_input.send_keys("19000")

    # Step 3: Find and click the "Get estimate" button
    get_estimate_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-0]")
    get_estimate_button.click()

    # Step 4: Wait and check the page title "Unfortunately, I have no matching contractors in your area yet."
    wait = WebDriverWait(driver, 10)
    element = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//h4[contains(text(),"Unfortunately, I have no matching contractors in your area yet.")]')))
    element_text = element.text
    assert "Unfortunately, I have no matching contractors in your area yet." in element_text


# Test_003 Check that we are blocking the flow and show the Warning message for a zero area value
def test_wrong_siding_area_value(driver):
    # Step 1: Open the website and check the title
    driver.get("https://hb-eta.stage.sirenltd.dev/siding")
    assert "Siding - HomeBuddy" in driver.title

    # Step 2: Find the zip code input field and enter a valid zip code
    zip_code_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-0]")
    zip_code_input.send_keys("09090")

    # Step 3: Find and click the "Get estimate" button
    get_estimate_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-0]")
    get_estimate_button.click()

    # Step 4: Wait and check the page title "Project type"
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What type of project is this?')]")))

    # Step 5: Check that "Next" button disabled until the type is selected
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 6: Select the type and click "Next"
    project_type1_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]")
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

    # Step 11: Input the area value and check Warning message, and "Next" button 
    siding_area_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-squarefeet-tel]")
    siding_area_input.clear()
    siding_area_input.send_keys("0")
    next_button = driver.find_element(By.XPATH, "//button[@data-autotest-button-submit-next]")

    # Find the element
    element = driver.find_element(By.XPATH, '//div[@data-state="focus" and @data-status="invalid"]')
    message = element.find_element(By.CLASS_NAME, 'customInput__message').text

    assert not next_button.is_enabled()  # Button should be disabled
    assert message == "Number can’t start with 0"  # Check the Warning message


# Test_004 Check the warning message for the 3+ stories in the house
def test_stories_warning(driver):
    # Step 1: Open the website and check the title
    driver.get("https://hb-eta.stage.sirenltd.dev/siding")
    assert "Siding - HomeBuddy" in driver.title

    # Step 2: Find the zip code input field and enter a valid zip code
    zip_code_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-0]")
    zip_code_input.send_keys("09090")

    # Step 3: Find and click the "Get estimate" button
    get_estimate_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-0]")
    get_estimate_button.click()

    # Step 4: Wait and check the page title "Project type"
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'What type of project is this?')]")))

    # Step 5: Check that "Next" button disabled until the type is selected
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 6: Select the type and click "Next"
    project_type1_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]")
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
    siding_area_input = driver.find_element(By.CSS_SELECTOR, "[data-autotest-input-squarefeet-tel]")
    siding_area_input.clear()
    siding_area_input.send_keys("42")
    next_button = driver.find_element(By.XPATH, "//button[@data-autotest-button-submit-next]")
    next_button.click()

    # Step 12: Wait and check the page title "Amount of stories", check the "Next" button
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
        (By.XPATH, "//h4[contains(text(),'How many stories is your house?')]")))
    next_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    assert not next_button.is_enabled()  # Button should be disabled

    # Step 13: Select the amount of stories "3+", check the warning message and yes/no buttons
    stories_amount4_radio = driver.find_element(By.CSS_SELECTOR, "[data-autotest-radio-sdstories-4]")
    driver.execute_script("arguments[0].click();", stories_amount4_radio)
    yes_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-submit-yes]")
    no_button = driver.find_element(By.CSS_SELECTOR, "[data-autotest-button-button-no]")

    # Find the element
    element = driver.find_element(By.XPATH, '//div[@class="px-0 px-md-8 mt-2 mt-md-0 mb-4 h4 text-center text-orangeDeep100"]')
    message = element.text

    expected_message = "Unfortunately our contractors don’t work on homes taller than three stories. Would you like to continue?"
    assert message == expected_message # Check the Warning message
    assert yes_button.is_enabled()
    assert no_button.is_enabled()
