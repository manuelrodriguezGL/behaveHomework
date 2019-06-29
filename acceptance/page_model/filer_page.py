from acceptance.locators.filer_page_locators import FilerPageLocators
from acceptance.page_model.base_page import BasePage


class FilerPage(BasePage):
    @property
    def filer_dropdown(self):
        return self.driver.find_element(*FilerPageLocators.FILER_DROPDOWN)

    @property
    def filer_search_box(self):
        return self.driver.find_element(*FilerPageLocators.FILER_SEARCH_BOX)

    @property
    def new_folder_button(self):
        return self.driver.find_element(*FilerPageLocators.NEW_FOLDER_BUTTON)

    @property
    def folder_names_column(self):
        return self.driver.find_elements(*FilerPageLocators.FOLDER_NAMES_COLUMN)

    @property
    def delete_folder_confirm_button(self):
        return self.driver.find_element(*FilerPageLocators.DELETE_FOLDER_CONFIRM_BUTTON)

    @property
    def folder_rows(self):
        return self.driver.find_elements(*FilerPageLocators.FOLDER_ROWS)

    @property
    def delete_folder_button(self):
        return FilerPageLocators.DELETE_FOLDER_BUTTON

    @property
    def folder_data_url_attrib(self):
        return FilerPageLocators.FOLDER_DATA_URL_ATTRIB

    @property
    def folder_data_name_attrib(self):
        return FilerPageLocators.FOLDER_DATA_NAME_ATTRIB

    @property
    def delete_button_href_attrib(self):
        return FilerPageLocators.DELETE_BUTTON_HREF_ATTRIB

