from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, "id_username")
    PASSWORD = (By.ID, "id_password")
    SUBMIT = (By.CSS_SELECTOR, "[type='submit']")
