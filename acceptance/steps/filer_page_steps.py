from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of
from re import findall

from acceptance.page_model.filer_page import FilerPage
from acceptance.utils.botstyle import find_text_on_collection

use_step_matcher('re')


@step('The folder management page loads')
def step_impl(context):
    context.execute_steps(f"""
            When I wait for 2 seconds
            Then I see the filer dropdown menu
            And I see the file search box 
        """)


@step('I see the filer dropdown menu')
def step_impl(context):
    try:
        page = FilerPage(context)
        visibility_of(page.filer_dropdown)
    except Exception as e:
        print(e.__cause__)


@step('I see the file search box')
def step_impl(context):
    try:
        page = FilerPage(context)
        visibility_of(page.filer_search_box)
    except Exception as e:
        print(e.__cause__)


@step('The folder name "(.*)" appears on Folders table')
def set_impl(context, text):
    page = FilerPage(context)
    assert find_text_on_collection(page.folder_names_column, text), "Folder not found!"


@step('I click on Remove button for "(.*)"')
def step_impl(context, text):
    try:
        page = FilerPage(context)
        folder_id = None
        for row in page.folder_rows:
            folder_data_name = row.get_attribute(page.folder_data_name_attrib)
            if folder_data_name == text:
                folder_id = findall('\d+', row.get_attribute(page.folder_data_url_attrib))[0]
                break
        delete_button = page.delete_folder_button.format(folder_id)
        context.driver.find_element_by_css_selector(delete_button).click()
    except Exception as e:
        context.logger.error(e.__cause__)


@step('I confirm folder deletion')
def step_impl(context):
    context.execute_steps(f"""
                When I wait for 2 seconds
                And I see the page header with text "Are you sure?"
                Then I click the confirm button 
            """)


@step('I click the confirm button')
def step_impl(context):
    try:
        page = FilerPage(context)
        page.delete_folder_confirm_button.click()
    except Exception as e:
        context.logger.info(e.__cause__)


@step('The folder name "(.*)" is not on Folders table anymore')
def step_impl(context, text):
    try:
        page = FilerPage(context)
        assert not find_text_on_collection(page.folder_names_column, text), "Unexpected folder found: {}!".format(text)
    except Exception as e:
        context.logger.info(e.__cause__)
