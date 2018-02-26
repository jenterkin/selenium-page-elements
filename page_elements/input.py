from page_elements import Element
from page_elements.decorators import web_element_method


class InputField(Element):
    @web_element_method
    def _monkey_patch_method(self):
        return self.get_attribute('value')

    def __set__(self, obj, value):
        super(InputField, self).__set__(obj, value)
        self.element.clear()
        self.element.send_keys(value)
