import allure
from selenium import webdriver

from acceptance.utils.logger import setup_custom_logger
from acceptance.utils.read_env_config import ReadEnvConfig


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

    if scenario.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    print('\n')


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

    context.driver.set_page_load_timeout(context.config.userdata.get('se_default_page_load_time'))
    context.driver.implicitly_wait(context.config.userdata.get('se_default_implicit_time'))
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


def before_rule(context, rule):
    print_custom(rule)


def after_tag(context, tag):
    if tag == "clean_something":
        print_custom("We are going to clean something right now")


def print_custom(text):
    print("\n\n******************************************************************************")
    print(text)
    print("******************************************************************************\n\n")
