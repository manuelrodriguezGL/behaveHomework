from acceptance.locators.users_page_locators import UsersPageLocators
from acceptance.page_model.base_page import BasePage


class UsersPage(BasePage):
    @property
    def get_header(self):
        return self.driver.find_element(*UsersPageLocators.HEADER_H1)

    @property
    def search_bar(self):
        return self.driver.find_element(*UsersPageLocators.SEARCHBAR_TEXT)

    @property
    def search_button(self):
        return self.driver.find_element(*UsersPageLocators.SEARCH_BUTTON)

    @property
    def users_result_table(self):
        return self.driver.find_element(*UsersPageLocators.USERS_RESULT_TABLE)

    @property
    def users_name_table(self):
        return self.driver.find_elements(*UsersPageLocators.USERS_TABLE_NAMES)
