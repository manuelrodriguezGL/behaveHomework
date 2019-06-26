from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.add_user_page import AddUserPage
from acceptance.utils.botstyle import wait_for_element_to_appear

use_step_matcher("re")


@step("I create a new user with the following information")
def step_impl(context):
    for row in context.table:
        context.execute_steps(f"""
            When I wait for 2 seconds
            And I fill username with value "{row['username']}"
            And I fill password with value "{row['password']}"
            And I fill password confirm with value "{row['password_confirmation']}"
        """)


@step("I click on SAVE button")
def step_impl(context):
    page = AddUserPage(context)
    page.save_button.click()
