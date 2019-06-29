from selenium.webdriver.common.by import By


class FilerPageLocators:
    FILER_DROPDOWN = (By.CSS_SELECTOR, ".filer-navigator-breadcrumbs-dropdown-container>a")
    FILER_SEARCH_BOX = (By.CSS_SELECTOR, ".filter-search-wrapper>.filter-files-field")
    NEW_FOLDER_BUTTON = (By.CSS_SELECTOR, ".navigator-button-wrapper>a[class='navigator-button']")
    FOLDER_NAMES_COLUMN = (By.CSS_SELECTOR, "td.column-name>div>a")
    DELETE_FOLDER_BUTTON = (By.CSS_SELECTOR, "td.column-action>a[href='/admin/filer/folder/2/delete/']")
