from selenium.webdriver.common.by import By


class UsersLocators:
    ADD_USER = By.CSS_SELECTOR, "[href^='/admin/auth/user/add/']"
    SELECT_ALL_CHECK = By.ID, "action-toggle"
    SEARCH_BAR = By.ID, "searchbar"
    SEARCH_BTN = By.CSS_SELECTOR, "#changelist-search [value='Search']"
    USERS_TABLE = By.ID, "result_list"
    ACTION_SELECT = By.NAME, "action"
    GO_BUTTON = By.NAME, "index"
