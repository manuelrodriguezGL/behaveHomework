from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_TEXT = (By.ID, "id_username")
    PASSWORD_TEXT = (By.ID, "id_password")
    LOGIN_BUTTON = (By.CSS, "input[type='submit']")
