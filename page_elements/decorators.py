from selenium.webdriver.remote.webelement import WebElement


def web_element_method(fn):
    '''
    Disallows method from being called on anything that is not an instance of
    `selenium.webdriver.remote.webelement.WebElement`.
    '''
    def wrapper(_, self=None):
        if self is None or not isinstance(self, WebElement):
            raise TypeError(
                    "Can only call `_monkey_patch_method` on a "
                    "`WebElement` instance")
        return fn(self)
    return wrapper
