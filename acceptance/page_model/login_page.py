from acceptance.locators.login_locators import LoginLocators
from acceptance.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def username(self):
        return self.driver.find_element(*LoginLocators.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocators.PASSWORD)

    @property
    def submit_btn(self):
        return self.driver.find_element(*LoginLocators.SUBMIT)
