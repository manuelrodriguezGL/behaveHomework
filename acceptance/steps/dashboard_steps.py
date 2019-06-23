from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.dashboard_page import DashboardPage

use_step_matcher('re')


@step('I should( not)? see logout option')
def step_impl(context, flag):
    page = DashboardPage(context)
    if flag:
        assert not visibility_of(page.logout)
    else:
        assert visibility_of(page.logout)


@step('I should( not)? see change password option')
def step_impl(context, flag):
    page = DashboardPage(context)
    if flag:
        assert not visibility_of(page.change_password)
    else:
        assert visibility_of(page.change_password)


@step('I logout the application')
def step_impl(context):
    page = DashboardPage(context)
    page.logout.click()


@step('I select Users link in dashboard')
def step_impl(context):
    page = DashboardPage(context)
    page.users_link.click()
