from acceptance.locators.dashboard_locators import DashboardLocators
from acceptance.page_model.base_page import BasePage


class DashboardPage(BasePage):
    @property
    def logout(self):
        return self.driver.find_element(*DashboardLocators.LOGOUT)

    @property
    def change_password(self):
        return self.driver.find_element(*DashboardLocators.CHANGE_PASSWORD)
