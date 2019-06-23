from behave import use_step_matcher, step

from acceptance.page_model.users_new_page import UsersNewPage
from acceptance.utils.botstyle import send_keys

use_step_matcher('re')


@step('For new user I fill username with value "(.*)"')
def step_impl(context, value):
    page = UsersNewPage(context)
    send_keys(page.username, value)


@step('For new user I fill password with value "(.*)"')
def step_impl(context, value):
    page = UsersNewPage(context)
    send_keys(page.password, value)


@step('For new user I fill password confirm with value "(.*)"')
def step_impl(context, value):
    page = UsersNewPage(context)
    send_keys(page.password_confirm, value)


@step('I save the new user')
def step_impl(context):
    page = UsersNewPage(context)
    page.save.click()
    page.save.click()
