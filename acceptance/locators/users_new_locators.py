from selenium.webdriver.common.by import By


class UsersNewLocators:
    USERNAME = By.ID, "id_username"
    PASSWORD = By.ID, "id_password1"
    PASSWORD_CONFIRM = By.ID, "id_password2"
    SAVE = By.CSS_SELECTOR, "[name='_save']"
