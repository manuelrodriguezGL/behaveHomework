from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.dashboard_page import DashboardPage

use_step_matcher('re')


@step('I should( not)? see logout option')
def step_impl(context, flag):
    page = DashboardPage(context)
    if flag:
        assert not visibility_of(page.logout_option)
    else:
        assert visibility_of(page.logout_option)


@step('I should( not)? see change password option')
def step_impl(context, flag):
    page = DashboardPage(context)
    if flag:
        assert not visibility_of(page.change_password_option)
    else:
        assert visibility_of(page.change_password_option)


@step('I click on Add option on Users dashboard')
def step_impl(context):
    page = DashboardPage(context)
    try:
        option = page.add_user_option
        option.click()
    except Exception as e:
        print(e.__cause__)


@step('I click on Folders option on Users dashboard')
def step_impl(context):
    page = DashboardPage(context)
    try:
        page.folders_option.click()
    except Exception as e:
        print(e.__cause__)


@step('I logout the application')
def step_impl(context):
    context.execute_steps(f"""
                When I click logout option
                And I click into the site name
                And I wait for 2 seconds
            """)


@step('I click logout option')
def step_impl(context):
    page = DashboardPage(context)
    page.logout_option.click()
