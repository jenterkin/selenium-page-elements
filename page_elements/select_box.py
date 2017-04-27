from selenium.webdriver.support.select import Select
from page_elements.base import Base


class SelectBox(Base):
    def __set__(self, obj, value):
        if self.driver is None:
            self.driver = obj.driver
        Select(self.element).select_by_value(value)
