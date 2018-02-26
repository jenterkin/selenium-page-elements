from selenium.webdriver.support.select import Select
from page_elements import Element
from page_elements.decorators import web_element_method


class SelectBox(Element):
    @web_element_method
    def _monkey_patch_method(self):
        return self.get_attribute('value')

    def __set__(self, obj, value):
        super(SelectBox, self).__set__(obj, value)
        Select(self.element).select_by_value(value)
