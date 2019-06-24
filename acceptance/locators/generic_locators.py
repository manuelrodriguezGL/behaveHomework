from selenium.webdriver.common.by import By


class GenericLocators:
    PAGE_NAME = (By.XPATH, "//h1[@id='site-name']/a")
    BUTTON_VALUE = "//*[value='{}']"
