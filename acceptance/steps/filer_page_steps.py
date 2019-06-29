from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.filer_page import FilerPage
from acceptance.utils.botstyle import wait_for_element_to_appear, find_text_on_collection

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
        wait_for_element_to_appear(context, page.filer_dropdown)
    except Exception as e:
        print(e.__cause__)


@step('I see the file search box')
def step_impl(context):
    try:
        page = FilerPage(context)
        wait_for_element_to_appear(context, page.filer_search_box)
    except Exception as e:
        print(e.__cause__)


@step('The folder name "(.*)" appears on Folders table')
def set_impl(context, text):
    page = FilerPage(context)
    assert find_text_on_collection(page.folder_names_column, text)