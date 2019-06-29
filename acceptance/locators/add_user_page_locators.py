from selenium.webdriver.common.by import By


class AddUserPageLocators:
    HEADER_1 = (By.CSS_SELECTOR, "h1")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password1']")
    PASSWORD_CONF_INPUT = (By.CSS_SELECTOR, "input[name='password2']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "input[name='_save']")
