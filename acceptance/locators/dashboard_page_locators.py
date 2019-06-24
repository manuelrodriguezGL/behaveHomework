from selenium.webdriver.common.by import By


class DashboardPageLocators:
    LOGOUT = (By.CSS_SELECTOR, "[href='/admin/logout/']")
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "[href='/admin/password_change/']")
    USERS_LINK = (By.CSS_SELECTOR, "[href='/admin/auth/user/']")
    ADD_USER_OPTION = (By.CSS_SELECTOR, "[href='/admin/auth/user/add/']")