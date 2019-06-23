from time import sleep

from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.select import Select

from acceptance.page_model.generic_page import GenericPage
from acceptance.page_model.users_page import UsersPage
from acceptance.utils.botstyle import send_keys
from acceptance.utils.custom_selenium_elements.table import Table

use_step_matcher('re')


@step('Add user button should be displayed')
def step_impl(context):
    page = UsersPage(context)
    assert visibility_of(page.add_user)


@step('I click on Add User button')
def step_impl(context):
    page = UsersPage(context)
    page.add_user.click()


@step('I search for user with name "(.*)"')
def step_impl(context, value):
    page = UsersPage(context)
    send_keys(page.search_bar, value)
    sleep(2)
    page.search_btn.click()


@step('The number of users displayed should be (\d+)')
def step_impl(context, value):
    page = UsersPage(context)
    table = Table(context, page.users_table)
    assert table.get_total_rows_number() == int(value), "The user was not found in the list"


@step('I remove user with name "(.*)" if exists')
def step_impl(context, value):
    page = UsersPage(context)
    context.execute_steps(f"When I search for user with name \"{value}\"")
    page.select_all_check.click()
    Select(page.action_select).select_by_visible_text("Delete selected users")
    page.go_button.click()
    generic_page = GenericPage(context)
    generic_page.button_with_value("Yes, I'm sure").click()
    sleep(2)
