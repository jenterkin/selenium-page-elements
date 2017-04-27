class Base:
    def __init__(self, by, selector):
        self.by = by
        self.selector = selector
        self.value = None
        self.driver = None

    def __get__(self, obj, objtype=None):
        if self.driver is None:
            self.driver = obj.driver
        return self.element.get_attribute('value')

    def __set__(self, obj, value):
        if self.driver is None:
            self.driver = obj.driver
        self.element.clear()
        self.element.send_keys(value)

    @property
    def element(self):
        return self.driver.find_element(self.by, self.selector)
