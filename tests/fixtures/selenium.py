import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get('file:///Users/jenterkin/repos/page_elements/tests/index.html')
    yield driver
    driver.close()
