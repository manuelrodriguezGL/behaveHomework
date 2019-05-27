from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def send_keys(element=None, text="", clear=True):
    """
    This method perform a custom send keys function
    :param element: The text field
    :param text: The text to put into the textfiel
    :param clear: If you want to clear the field or not, it is True by default
    :return: N/A
    """
    if clear:
        element.clear()
    element.send_keys(text)


def wait_for_element_to_disappear(context, element, timeout=0):
    """
    This method waits for element to disappear of the page
    :param context: The behave context instance
    :param element: The element to wait to disappear
    :param timeout: The time to wait until the element is not present
    :return: N/A
    """
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
            context.driver.implicitly_wait(context.config.userdata.get('se_default_implicit_time'))
        return element


def wait_for_element_appear(context, element, timeout=0):
    """
    This method waits for element to be present in the page
    :param context: The behave context instance
    :param element: The element to wait to appear
    :param timeout: The time to wait until the element is present
    :return:
    """
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
            context.driver.implicitly_wait(context.config.userdata.get('se_default_implicit_time'))
        return element


def mouse_hover(context, element):
    """
    This method perform a "mousehover" on a given element
    :param context: The behave context instance
    :param element: The element to perform the mousehover action
    :return: N/A
    """
    ActionChains(context.driver).move_to_element(element).perform()


def double_click(context, element):
    """
    This method perform a "double click" on a given element
    :param context: The behave context instance
    :param element: The element to perform the double click action
    :return: N/A
    """
    ActionChains(context.driver).double_click(element).perform()
