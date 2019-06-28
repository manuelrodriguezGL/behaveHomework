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


@step('I click button with value "(.*)"')
def step_impl(context, value):
    page = GenericPage(context)
    page.button_vale(value).click()


@step("I wait for 2 seconds")
def step_impl(context):
    explicit_wait(2)
