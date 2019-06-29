from behave import use_step_matcher, step

from acceptance.page_model.filer_page import FilerPage
from acceptance.page_model.new_folder_page import NewFolderPage
from acceptance.utils.botstyle import send_keys

use_step_matcher('re')

main_window = None
window_new = None


@step('I create a new folder and click Save button')
def step_impl(context):
    try:
        for row in context.table:
            context.execute_steps(f"""
                When I click on New Folder option
                Then Add new folder window is opened
                When I fill folder name with value "{row['username']}"
                And I click Save button on new folder page
                And I return to main window
            """)
    except Exception as e:
        context.logger.info(e.__cause__)


@step('I click on New Folder option')
def step_impl(context):
    try:
        FilerPage(context).new_folder_button.click()
    except Exception as e:
        print(e.__cause__)


@step('Add new folder window is opened')
def step_impl(context):
    driver = context.driver
    main_window = driver.window_handles[0]  # Gets the main window
    window_new = driver.window_handles[1]
    driver.switch_to.window(window_new)


@step('I fill folder name with value "(.*)"')
def step_impl(context, text):
    try:
        page = NewFolderPage(context)
        send_keys(page.folder_name_textbox, text)
    except Exception as e:
        context.logger.info(e.__cause__)


@step('I click Save button on new folder page')
def step_impl(context):
    try:
        page = NewFolderPage(context)
        page.folder_save_button.click()
    except Exception as e:
        context.logger.info(e.__cause__)


@step('I return to main window')
def step_impl(context):
    try:
        context.driver.switch_to.window(main_window)
    except Exception as e:
        context.logger.info(e.__cause__)
