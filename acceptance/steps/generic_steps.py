from time import sleep

from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.generic_page import GenericPage

use_step_matcher('re')


@step('I should( not)? see( exact)? text "(.*)"')
def step_impl(context, no_flag, exact_flag, text):
    page = GenericPage(context)

    if no_flag:
        assert not page.element_with_text(text, True if exact_flag else False), "The text should NOT be displayed but it is."
    else:
        assert visibility_of(page.element_with_text(text, True if exact_flag else False)), "The text should be displayed but it is NOT."


@step('I click into the site name')
def step_impl(context):
    page = GenericPage(context)
    if page.page_site_name():
        page.page_site_name().click()


@step('I wait (\d+) seconds')
def step_impl(context, time_in_seconds):
    sleep(int(time_in_seconds))


@step('I click button with value "(.*)"')
def step_impl(context, value):
    page = GenericPage(context)
    page.button_with_value(value).click()
