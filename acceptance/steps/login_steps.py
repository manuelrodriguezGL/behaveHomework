from behave import use_step_matcher, step

from acceptance.page_model.login_page import LoginPage
from acceptance.utils.botstyle import send_keys

use_step_matcher('re')


@step('I login with username "(.*)" and password "(.*)"')
def step_impl(context, username, password):
    page = LoginPage(context)

    if username == "valid_user":
        send_keys(element=page.username, text=context.app_username)
    else:
        send_keys(page.username, username)

    if password == "valid_password":
        send_keys(element=page.password, text=context.app_password)
    else:
        send_keys(page.password, password)
    page.submit_btn.submit()
