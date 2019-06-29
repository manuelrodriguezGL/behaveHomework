from selenium.webdriver.common.by import By


class NewFolderPageLocators:
    PAGE_HEADER_TEXT = "Add new folder"
    FOLDER_NAME_TEXTBOX = (By.CSS_SELECTOR, "input[id='id_name']")
    FOLDER_SAVE_BUTTON = (By.CSS_SELECTOR, "input[name='_save']")
