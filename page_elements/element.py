from types import MethodType
from selenium.webdriver.support.ui import WebDriverWait


class Element(object):
    def __init__(self, by, selector, wait=None, wait_timeout=10):
        self.by = by
        self.obj = None
        self.selector = selector
        self.value = None
        self.wait = wait
        self.wait_timeout = wait_timeout

    def __get__(self, obj, objtype=None):
        self.obj = obj
        return self._monkey_patch(self.element)

    def __set__(self, obj, value):
        self.obj = obj

    def _monkey_patch_method(self, element):
        raise NotImplementedError

    def _monkey_patch(self, element):
        element.value = MethodType(self._monkey_patch_method, element)
        return element

    @property
    def element(self):
        if self.wait is not None:
            return \
                WebDriverWait(self.obj.driver, self.wait_timeout).until(
                    self.wait((self.by, self.selector))
                )
        return self.obj.driver.find_element(self.by, self.selector)
