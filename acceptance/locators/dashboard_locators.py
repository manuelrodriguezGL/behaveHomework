from selenium.webdriver.common.by import By


class DashboardLocators:
    LOGOUT = (By.CSS_SELECTOR, "[href='/admin/logout/']")
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "[href='/admin/password_change/']")
    USERS_LINK = By.CSS_SELECTOR, "#content-main .module th [href='/admin/auth/user/']"
