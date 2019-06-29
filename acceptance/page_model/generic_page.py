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
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_wait'))
            return result

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

    def page_header(self):
        result = None
        try:
            self.context.driver.implicitly_wait(5)
            result = self.driver.find_element(*GenericLocators.PAGE_HEADER)
        except Exception as e:
            self.context.logger.error(e.__class__)
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_wait'))
            return result

    def element_with_text(self, text, exact_flag=False):
        result = None
        try:
            self.context.driver.implicitly_wait(5)
            if exact_flag:
                result = self.driver.find_element(By.XPATH, GenericLocators.ELEMENT_WITH_EXACT_TEXT.format(text))
            else:
                result = self.driver.find_element(By.XPATH, GenericLocators.ELEMENT_CONTAINS_TEXT_ONLY.format(text))
        except Exception as e:
            self.context.logger(e.__class__)
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_wait'))
            return result

    def element_and_text(self, element_path, text):
        result = None
        try:
            self.context.driver.implicitly_wait(5)
            result = self.driver.find_element(By.XPATH,
                                              GenericLocators.ELEMENT_CONTAINS_TEXT.format(element_path, text))
        except Exception as e:
            self.context.logger(e.__class__)
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_wait'))
            return result

    def button_value(self, value):
        try:
            return self.driver.find_element(By.XPATH, GenericLocators.BUTTON_VALUE.format(value))
        except:
            return None
