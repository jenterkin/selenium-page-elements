from types import MethodType
from selenium.webdriver.remote.webelement import WebElement


class Element:
    def __init__(self, by, selector):
        self.by = by
        self.obj = None
        self.selector = selector
        self.value = None

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
        elem = self.obj.driver.find_element(self.by, self.selector)
        return elem
