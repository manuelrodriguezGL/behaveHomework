from acceptance.locators.login_locators import LoginLocators
from acceptance.locators.users_locators import UsersLocators
from acceptance.page_model.base_page import BasePage


class UsersPage(BasePage):
    @property
    def add_user(self):
        return self.driver.find_element(*UsersLocators.ADD_USER)

    @property
    def search_bar(self):
        return self.driver.find_element(*UsersLocators.SEARCH_BAR)

    @property
    def search_btn(self):
        return self.driver.find_element(*UsersLocators.SEARCH_BTN)

    @property
    def users_table(self):
        return self.driver.find_element(*UsersLocators.USERS_TABLE)

    @property
    def select_all_check(self):
        return self.driver.find_element(*UsersLocators.SELECT_ALL_CHECK)

    @property
    def action_select(self):
        return self.driver.find_element(*UsersLocators.ACTION_SELECT)

    @property
    def go_button(self):
        return self.driver.find_element(*UsersLocators.GO_BUTTON)
