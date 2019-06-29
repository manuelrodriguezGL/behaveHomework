from acceptance.locators.new_folder_page_locators import NewFolderPageLocators
from acceptance.page_model.base_page import BasePage


class NewFolderPage(BasePage):
    @property
    def page_header_text(self):
        return NewFolderPageLocators.PAGE_HEADER_TEXT

    @property
    def folder_name_textbox(self):
        return self.driver.find_element(*NewFolderPageLocators.FOLDER_NAME_TEXTBOX)

    @property
    def folder_save_button(self):
        return self.driver.find_element(*NewFolderPageLocators.FOLDER_SAVE_BUTTON)
