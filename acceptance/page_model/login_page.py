from acceptance.locators.login_page_locators import LoginPageLocators
from acceptance.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def username_text(self):
        return self.driver.find_element(*LoginPageLocators.USERNAME_TEXT)

    @property
    def password_text(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_TEXT)

    @property
    def login_button(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
