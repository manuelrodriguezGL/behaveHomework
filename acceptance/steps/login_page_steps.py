from behave import use_step_matcher, step

from acceptance.page_model.login_page import LoginPage
from acceptance.utils.botstyle import send_keys


use_step_matcher("re")


@step('I login with username "(.*)" and password "(.*)"')
def step_impl(context, username, password):
    page = LoginPage(context)

    send_keys(page.username_text, username)
    send_keys(page.password_text, password)

    page.login_button.submit()
