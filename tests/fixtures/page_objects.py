import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from page_elements import InputField, TextArea, SelectBox, CheckBox, Element


class BasePageObject(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://webserver:8000')


class PageObject(BasePageObject):
    input_field = InputField(By.ID, 'input')
    textarea = TextArea(By.ID, 'textarea')
    select_box = SelectBox(By.ID, 'select')
    checkbox = CheckBox(By.ID, 'checkbox')
    input_field_wait = InputField(
        By.ID, 'input', wait=EC.presence_of_element_located)


@pytest.fixture(scope='session')
def page_object(driver):
    return PageObject(driver)


@pytest.fixture(scope='session')
def page_object_with_wait(driver):
    return PageObjectWithWait(driver)
