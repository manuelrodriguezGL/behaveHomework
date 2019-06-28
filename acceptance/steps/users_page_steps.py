from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.users_page import UsersPage
from acceptance.utils.botstyle import send_keys, explicit_wait, find_text_on_collection

use_step_matcher('re')


@step('I search for "(.*)" on search box')
def step_impl(context, text):
    page = UsersPage(context)
    send_keys(page.search_bar, text)
    explicit_wait(2)
    page.search_button.click()


@step('I see "(.*)" displayed on results grid')
def step_impl(context, text):
    page = UsersPage(context)
    assert find_text_on_collection(page.users_name_table, text)
