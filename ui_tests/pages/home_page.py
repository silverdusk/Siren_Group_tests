from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://test.com"

    def navigate_to_home(self):
        self.driver.get(self.url)