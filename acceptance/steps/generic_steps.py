from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.generic_page import GenericPage
from acceptance.utils.botstyle import explicit_wait

use_step_matcher('re')


@step('I see the page name displayed')
def step_impl(context):
    page = GenericPage(context)
    assert visibility_of(page.page_name())


@step('I see the page header with text "(.*)"')
def step_impl(context, text):
    page = GenericPage(context)
    assert visibility_of(page.element_and_text(page.page_header(), text))


@step('I wait for 2 seconds')
def step_impl(context):
    explicit_wait(2)


@step('I click into the site name')
def step_impl(context):
    page = GenericPage(context)
    if page.page_site_name():
        page.page_site_name().click()
