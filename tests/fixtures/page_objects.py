import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from page_elements import InputField, TextArea, SelectBox, CheckBox


class PageObject():
    input_field = InputField(By.ID, 'input')
    textarea = TextArea(By.ID, 'textarea')
    select_box = SelectBox(By.ID, 'select')
    checkbox = CheckBox(By.ID, 'checkbox')

    def __init__(self, driver=None):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get('http://webserver:8000')


@pytest.fixture(scope='session')
def page_object(request):
    page_object = PageObject()
    def fin():
        page_object.driver.quit()
    request.addfinalizer(fin)
    return page_object
