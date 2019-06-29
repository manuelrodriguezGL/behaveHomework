from behave import use_step_matcher, step

from acceptance.page_model.change_user_page import ChangeUserPage

use_step_matcher('re')


@step('I click on SAVE button again')
def step_impl(context):
    page = ChangeUserPage(context)
    page.save_button.click()
