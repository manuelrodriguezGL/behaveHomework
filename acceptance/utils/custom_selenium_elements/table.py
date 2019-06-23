from selenium.webdriver.common.by import By


class Table:

    def __init__(self, context, table_as_web_element):
        self.table = table_as_web_element
        self.driver = context.driver
        self.context = context

    def exist_column_header(self, column_header_text):
        """
        This method checks if a column exists or not in a table grid
        :param column_header_text: The text to check if exists or not
        :return: True / False depending on if the column exists or not
        """
        headers = self.table.find_elements(By.XPATH, ".//th")
        for header in headers:
            if header.text == column_header_text:
                return True
        return False

    def get_header_index(self, header_text):
        """
        This method gets the header index in the table to map the table rows
        :param header_text: The header text to find
        :return: The index of the header
        """
        headers = self.table.find_elements(By.XPATH, ".//th")
        index = 0
        for header in headers:
            index += 1
            if header.text == header_text:
                return index
        return -1

    def get_cell_by_col_and_row(self, row, col):
        return self.table.find_element(By.XPATH, ".//tbody//tr[{}]/td[{}]".format(row, col))

    def get_table_rows_with_value_in_column(self, column, value):
        index = self.get_header_index(column)
        return self.table.find_elements(By.XPATH,
                                        ".//tbody//tr/td[{}]/*[contains(text(),'{}')]/ancestor::tr[position()=1]".format(index, value))

    def get_delete_link(self, row, time_in_seconds=-1):
        try:
            if time_in_seconds != -1:
                self.context.driver.implicitly_wait(time_in_seconds)
            index = self.get_header_index('Actions')
            result = row.find_element(By.XPATH, ".//td[{}]//*[text()='Delete']".format(index))
        except:
            result = None
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_time'))
        return result

    def get_edit_link(self, row, time_in_seconds=-1):
        try:
            if time_in_seconds != -1:
                self.context.driver.implicitly_wait(time_in_seconds)
            index = self.get_header_index('Actions')
            result = row.find_element(By.XPATH, ".//td[{}]//*[text()='Edit']".format(index))
        except:
            result = None
        finally:
            self.context.driver.implicitly_wait(self.context.config.userdata.get('se_default_implicit_time'))
        return result

    def get_check_box(self, row):
        try:
            index = self.get_header_index('Selected')
            return row.find_element(By.XPATH, ".//td[{}]//input[@type='checkbox']".format(index))
        except:
            return None

    def get_total_rows_number(self):
        return len(self.table.find_elements(By.XPATH, ".//tr/td/.."))

