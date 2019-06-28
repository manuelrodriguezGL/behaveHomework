from behave import use_step_matcher, step
from selenium.webdriver.support.expected_conditions import visibility_of

from acceptance.page_model.change_user_page import ChangeUserPage
from acceptance.utils.botstyle import wait_for_element_to_appear


use_step_matcher('re')


@step('I click on SAVE button again')
def step_impl(context):
    page = ChangeUserPage(context)
    page.save_button.click()
