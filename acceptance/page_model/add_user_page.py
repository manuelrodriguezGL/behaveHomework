from acceptance.locators.add_user_page_locators import AddUserPageLocators
from acceptance.page_model.base_page import BasePage


class AddUserPage(BasePage):
    @property
    def get_header(self):
        return self.driver.find_element(*AddUserPageLocators.HEADER_1)

    @property
    def username_input(self):
        return self.driver.find_element(*AddUserPageLocators.USERNAME_INPUT)

    @property
    def password_input(self):
        return self.driver.find_element(*AddUserPageLocators.PASSWORD_INPUT)

    @property
    def password_conf_input(self):
        return self.driver.find_element(*AddUserPageLocators.PASSWORD_CONF_INPUT)

    @property
    def save_button(self):
        return self.driver.find_element(*AddUserPageLocators.SAVE_BUTTON)
