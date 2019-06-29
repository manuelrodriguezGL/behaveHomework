from acceptance.locators.dashboard_page_locators import DashboardPageLocators
from acceptance.page_model.base_page import BasePage


class DashboardPage(BasePage):
    @property
    def logout_option(self):
        return self.driver.find_element(*DashboardPageLocators.LOGOUT_OPTION)

    @property
    def change_password_option(self):
        return self.driver.find_element(*DashboardPageLocators.CHANGE_PASSWORD_OPTION)

    @property
    def users_link(self):
        return self.driver.find_element(*DashboardPageLocators.USERS_LINK)

    @property
    def add_user_option(self):
        return self.driver.find_element(*DashboardPageLocators.ADD_USER_OPTION)

    @property
    def folders_option(self):
        return self.driver.find_element(*DashboardPageLocators.FOLDER_OPTION)
