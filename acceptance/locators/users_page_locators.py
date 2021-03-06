from selenium.webdriver.common.by import By


class UsersPageLocators:
    HEADER_H1 = (By.CSS_SELECTOR, "h`")
    SEARCHBAR_TEXT = (By.ID, "searchbar")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[value='Search']")
    USERS_RESULT_TABLE = (By.ID, "result_list")
    USERS_TABLE_NAMES = (By.CSS_SELECTOR, "#result_list>tbody>tr>th.field-username>a")
