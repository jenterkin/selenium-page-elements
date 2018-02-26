from page_elements import Element
from page_elements.decorators import web_element_method


class CheckBox(Element):
    @web_element_method
    def _monkey_patch_method(self):
        return self.is_selected()

    def __set__(self, obj, value):
        super(CheckBox, self).__set__(obj, value)
        if (value is True and not self.element.is_selected()) or \
           (value is False and self.element.is_selected()):
               self.element.click()
