from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def element_exist_xpath(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        return True
    except NoSuchElementException:
        return False
def element_exist_css(driver, css):
    try:
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return True
    except NoSuchElementException:
        return False
