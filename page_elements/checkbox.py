from page_elements.base import Base


class CheckBox(Base):
    def __get__(self, obj, objtype=None):
        if self.driver is None:
            self.driver = obj.driver
        return self.element.is_selected()

    def __set__(self, obj, value):
        if self.driver is None:
            self.driver = obj.driver
        if (value is True and not self.element.is_selected()) or \
           (value is False and self.element.is_selected()):
               self.element.click()
