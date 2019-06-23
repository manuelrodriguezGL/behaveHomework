from selenium.webdriver.common.by import By


class GenericLocators:
    ELEMENT_WITH_EXACT_TEXT = "//*[text()='{}']"
    ELEMENT_WITH_TEXT_CONTAINS = "//*[contains(text(),'{}')]"
    PAGE_SITE_NAME = By.XPATH, "//h1[@id='site-name']/a"
    BUTTON_WITH_VALUE = '//*[@value="{}"]'

