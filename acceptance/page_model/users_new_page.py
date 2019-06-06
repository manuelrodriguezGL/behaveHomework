from acceptance.locators.login_locators import LoginLocators
from acceptance.locators.users_locators import UsersLocators
from acceptance.locators.users_new_locators import UsersNewLocators
from acceptance.page_model.base_page import BasePage


class UsersNewPage(BasePage):
    @property
    def username(self):
        return self.driver.find_element(*UsersNewLocators.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*UsersNewLocators.PASSWORD)

    @property
    def password_confirm(self):
        return self.driver.find_element(*UsersNewLocators.PASSWORD_CONFIRM)

    @property
    def save(self):
        return self.driver.find_element(*UsersNewLocators.SAVE)
