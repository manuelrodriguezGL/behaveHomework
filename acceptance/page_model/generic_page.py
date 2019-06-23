from selenium.webdriver.common.by import By

from acceptance.locators.generic_locators import GenericLocators
from acceptance.page_model.base_page import BasePage


class GenericPage(BasePage):

    def page_site_name(self):
        result = None
        try:
            self.context.driver.implicitly_wait(5)
            result = self.driver.find_element(*GenericLocators.PAGE_SITE_NAME)
        except Exception as e:
            self.context.logger.error(e.__class__)
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_time'))
            return result

    def element_with_text(self, text, exact_match=False):
        result = None
        try:
            self.context.driver.implicitly_wait(5)
            if exact_match:
                result = self.driver.find_element(By.XPATH, GenericLocators.ELEMENT_WITH_EXACT_TEXT.format(text))
            else:
                result = self.driver.find_element(By.XPATH, GenericLocators.ELEMENT_WITH_TEXT_CONTAINS.format(text))
        except Exception as e:
            self.context.logger(e.__class__)
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_time'))
            return result

    def button_with_value(self, value):
        try:
            return self.driver.find_element(By.XPATH, GenericLocators.BUTTON_WITH_VALUE.format(value))
        except:
            return None
