from time import sleep
from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.generic_page import GenericPage

use_step_matcher("re")

@step("I see the page name displayed")
def step_impl(context):
    page = GenericPage(context)
    assert visibility_of(page.page_name())

@step("I click button with value '(.*)'")
def step_impl(context, value):
    page = GenericPage(context)
    page.button_vale(value).click()
