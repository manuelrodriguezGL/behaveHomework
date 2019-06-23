from time import sleep

from behave import use_step_matcher, step
from selenium.webdriver.support import select
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.select import Select

from acceptance.page_model.generic_page import GenericPage
from acceptance.page_model.login_page import LoginPage
from acceptance.page_model.users_page import UsersPage
from acceptance.utils.botstyle import send_keys
from acceptance.utils.custom_selenium_elements.table import Table

use_step_matcher('re')


@step('I create a new user with the following information')
def step_impl(context):
    for row in context.table:
        context.execute_steps(f"""
            When I click on Add User button
            And I wait 2 seconds
            And For new user I fill username with value "{row['username']}"
            And For new user I fill password with value "{row['password']}"
            And For new user I fill password confirm with value "{row['password']}"
            And I save the new user
            Then Add user button should be displayed
            When I search for user with name "{row['username']}"
        """)
