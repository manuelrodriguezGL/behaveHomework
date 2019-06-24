from selenium.webdriver.common.by import By

from acceptance.locators.generic_locators import GenericLocators
from acceptance.page_model.base_page import BasePage

class GenericPage(BasePage):
    def page_name(self):
        result = None
        try:
            self.context.driver.implicitly_wait(5)
            result = self.driver.find_element(*GenericLocators.PAGE_NAME)
        except Exception as e:
            self.context.logger.error(e.__class__)
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_wait'))
            return result

    def button_vale(self, value):
        try:
            return self.driver.find_element(By.XPATH, GenericLocators.BUTTON_VALUE.format(value))
        except:
            return None
