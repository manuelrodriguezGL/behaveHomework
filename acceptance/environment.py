import os

import allure
from selenium import webdriver

from acceptance.utils.logger import setup_custom_logger
from acceptance.utils.read_env_config import ReadEnvConfig
from api.pageobjects.filer_page_api import FilerPage
from api.pageobjects.user_page_api import UsersPage
from api.testcases.test_user_suite import TestUserSuite


def before_all(context):
    print_custom("Into before all hook")

    # define the logger instance
    context.logger = setup_custom_logger('automation_log')
    context.logger.info("************************************************************************************************")
    context.logger.info("* Starting execution of Automation..".upper())
    context.logger.info("************************************************************************************************")
    context.logger.info("Before all execution configurations -- setting environment..")

    # reading importante base variables
    context.app_username = context.config.userdata.get('app_username') or ReadEnvConfig.get_app_username(context)
    context.app_password = context.config.userdata.get('app_password') or ReadEnvConfig.get_app_password(context)
    context.app_url = context.config.userdata.get('app_url')
    context.browser = context.config.userdata.get('browser')


def after_all(context):
    print_custom("Into after all hook")


def before_step(context, step):
    step_start_status = step.status.name


def after_step(context, step):
    step_finish_status = step.status.name


def before_scenario(context, scenario):
    scenario_start_status = scenario.status


def after_scenario(context, scenario):
    scenario_finish_status = scenario.status

    # take screenshot if the test case fails
    if scenario.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    print('\n')

    # logout of the application if logout tag present
    # if "logout" in [tag for tag in scenario.tags]:
    #     context.execute_steps(f"""
    #         When I logout the application
    #         And I click into the site name
    #         And I wait 2 seconds
    #     """)
    context.logger.info("********************************************************************")
    context.logger.info(f"* Finished test case {scenario.name}")
    context.logger.info("********************************************************************")


def before_feature(context, feature):
    feature_before = feature.duration

    if context.config.userdata.get('browser') == 'firefox':
        ff_options = webdriver.FirefoxOptions()

        if context.config.userdata.get('se_headless') == "True":
            ff_options.add_argument('--headless')

        path = context.config.userdata.get('geckodriver_path')
        if path == "":
            context.driver = webdriver.Firefox(firefox_options=ff_options)
        else:
            context.driver = webdriver.Firefox(executable_path=path, firefox_options=ff_options)
        context.logger.info(
            "We are using 'Firefox' as a browser with driver version: {}".format(context.driver.desired_capabilities['moz:geckodriverVersion']))
    elif context.config.userdata.get('browser') == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if context.config.userdata.get('se_headless') == "True":
            chrome_options.add_argument('--headless')

        path = context.config.userdata.get('chromedriver_path')
        if path == "":
            context.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            context.driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        context.logger.info("We are using 'Chrome' as a browser with driver version: {}".format(context.driver.capabilities['version']))

    try:
        context.driver.maximize_window()
    except Exception as e:
        context.logger.error(e.__class__)
        context.logger.warning("Unable to maximize the browser. ")

    context.driver.set_page_load_timeout(context.config.userdata.get('se_default_page_load_wait'))
    context.driver.implicitly_wait(context.config.userdata.get('se_default_implicit_wait'))
    context.driver.delete_all_cookies()
    context.driver.get(context.app_url)


def after_feature(context, feature):
    feature_after = feature.duration
    context.logger.info("Closing the browser")
    context.driver.close()
    context.driver.quit()


def before_tag(context, tag):
    if tag == "smoke":
        print_custom("This is part of a smoke testing")

    if tag == "folders.remove_successful_ui":
        create_folder_api(context)


def before_rule(context, rule):
    print_custom(rule)


def after_tag(context, tag):
    if tag == "users.add_successful":
        delete_user_api(context)

    if tag == "folders.create_successful":
        delete_folder_api(context)

# context.execute_steps(f"""
        #     Given I login with username "valid_user" and password "valid_password"
        #     When I wait 2 seconds
        #     And I select Users link in dashboard
        #     And I remove user with name "{context.scenario.name}" if exists
        #     And I logout the application
        #     And I click into the site name
        #     And I wait 2 seconds
        # """)


def print_custom(text):
    print("\n\n******************************************************************************")
    print(text)
    print("******************************************************************************\n\n")


def delete_user_api(context):
    page = UsersPage(ReadEnvConfig.get_app_api_url(), context.app_username, context.app_password)
    user_id = page.get_user_id_by_username_contains(context.scenario.name)
    context.logger.info("*** Found User Id {} ***".format(user_id))
    context.logger.info("*** Deleting User Id {}... ***".format(user_id))
    page.delete_user(user_id)
    context.logger.info("*** User Id {} has been deleted! ***".format(user_id))


def delete_folder_api(context):
    page = FilerPage(ReadEnvConfig.get_app_api_url(), context.app_username, context.app_password)
    folder_id = page.get_folder_id_by_foldername_contains(context.scenario.name)
    context.logger.info("*** Found Folder Id {} ***".format(folder_id))
    context.logger.info("*** Deleting Folder Id {}... ***".format(folder_id))
    page.delete_folder(folder_id)
    context.logger.info("*** Folder Id {} has been deleted! ***".format(folder_id))


def create_folder_api(context):
    context.logger.info("{}".format(os.listdir()))
    page = FilerPage(ReadEnvConfig.get_app_api_url(), context.app_username, context.app_password)
    response_code = page.create_folder()
    context.logger.info("*** Folder creation returned response code: {} ***".format(response_code))
