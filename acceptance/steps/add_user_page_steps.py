from behave import use_step_matcher, step

from acceptance.page_model.add_user_page import AddUserPage
from acceptance.utils.botstyle import send_keys

use_step_matcher('re')


@step('I create a new user with the following information')
def step_impl(context):
    for row in context.table:
        context.execute_steps(f"""
            When I wait for 2 seconds
            And I fill username with value "{row['username']}"
            And I fill password with value "{row['password']}"
            And I fill password confirm with value "{row['password_confirmation']}"
        """)


@step('I click on SAVE button')
def step_impl(context):
    page = AddUserPage(context)
    page.save_button.click()


@step('I fill username with value "(.*)"')
def step_impl(context, text):
    page = AddUserPage(context)
    send_keys(page.username_input, text)


@step('I fill password with value "(.*)"')
def step_impl(context, text):
    page = AddUserPage(context)
    send_keys(page.password_input, text)


@step('I fill password confirm with value "(.*)"')
def step_impl(context, text):
    page = AddUserPage(context)
    send_keys(page.password_conf_input, text)
