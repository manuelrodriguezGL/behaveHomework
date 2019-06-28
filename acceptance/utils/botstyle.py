from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep


def send_keys(element=None, text="", clear=True):
    if clear:
        element.clear()
    element.send_keys(text)


def wait_for_element_to_disappear(context, element, timeout=0):
    try:
        if timeout != 0:
            context.driver.implicitly_wait(5)

        WebDriverWait(driver=context.driver, timeout=float(timeout)).until(
            expected_conditions.invisibility_of_element_located(element)
        )
    except Exception as e:
        element = None
        print(e.__cause__)
    finally:
        if timeout != 0:
            context.driver.implicitly_wait(context.config.userdata.get("se_default_implicit_time"))
        return element


def wait_for_element_to_appear(context, element, timeout=0):
    try:
        if timeout != 0:
            context.driver.implicitly_wait(5)

        WebDriverWait(driver=context.driver, timeout=float(timeout)).until(
            expected_conditions.visibility_of_element_located(element)
        )
    except Exception as e:
        element = None
        print(e.__cause__)
    finally:
        if timeout != 0:
            context.driver.implicitly_wait(context.config.userdata.get("se_default_implicit_time"))
        return element


def double_click(context, element):
    ActionChains(context.driver).double_click(element).perform()


def explicit_wait(seconds=1):
    sleep(seconds)


def find_text_on_collection(collection, text):
    found = False
    for element in collection:
        if element.text == text:
            found = True
    return found
