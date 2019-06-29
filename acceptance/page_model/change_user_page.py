from acceptance.locators.change_user_page_locators import ChangeUserPageLocators
from acceptance.page_model.base_page import BasePage


class ChangeUserPage(BasePage):
    @property
    def get_header(self):
        return self.driver.find_element(*ChangeUserPageLocators.HEADER_H1)

    @property
    def save_button(self):
        return self.driver.find_element(*ChangeUserPageLocators.SAVE_BUTTON)
