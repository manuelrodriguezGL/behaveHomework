from selenium.webdriver.common.by import By


class GenericLocators:
    ELEMENT_WITH_EXACT_TEXT = "//*[text()='{}']"
    ELEMENT_CONTAINS_TEXT_ONLY = "//*[contains(text(),'{}')]"
    ELEMENT_CONTAINS_TEXT = "//'{}'[contains(text(),'{}')]"
    PAGE_NAME = (By.XPATH, "//h1[@id='site-name']/a")
    PAGE_HEADER = (By.XPATH, "//div[@id='content']/h1")
    BUTTON_VALUE = "//*[value='{}']"
