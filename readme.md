# Selenium Page Elements

[![Build Status](https://travis-ci.org/jenterkin/selenium-page-elements.svg?branch=master)](https://travis-ci.org/jenterkin/selenium-page-elements)
[![codecov](https://codecov.io/gh/jenterkin/selenium-page-elements/branch/master/graph/badge.svg)](https://codecov.io/gh/jenterkin/selenium-page-elements)
[![PyPI version](https://badge.fury.io/py/selenium-page-elements.svg)](https://badge.fury.io/py/selenium-page-elements)

## Installation
```
$ pip install selenium-page-elements
```

## Overview
Selenium Page Elements is a thin wrapper around the Selenium python library that aims to make Page Objects quick and easy to create and maintain by allowing you to define and interact with web elements like object attributes.

```python
# Page Object
from selenium.webdriver.common.by import By
from page_elements import Element, InputField, CheckBox


class LoginPage:
    url = "http://localhost/login"

    # Define your elements in your class.
    username = InputField(By.ID, 'username')
    password = InputField(By.ID, 'password')
    stay_signed_in = CheckBox(By.ID, 'stay-signed-in')
    login_button = Element(By.XPATH, '//button[contains(text(), "Login")]')

    def __init__(self, driver):
        # Ensure that your page object has a Selenium webdriver in `self.driver`.
        self.driver = driver

    def open(self):
        self.driver.get(LoginPage.url)

    def login(self, username, password, stay_signed_in=True):
        # Use your elements just as you would any Python variable.
        self.username = username
        self.password = password
        self.keep_me_signed_in = stay_signed_in
        self.login_button.click()
```

The element classes take in a Selenium `By` object and a selector, so you can select any element you would be able to with Selenium.

To check the value of an element simply call the element with `.value()`
```python
    login_page = LoginPage(driver)
    login_page.username = 'mmario'
    print(login_page.username.value()) # prints 'mmario'
```

The reason you have to call `.value()` on the element is because Selenium Page Elements simply returns a monkey-patched Selenium `WebElement` instance. The reason for returning the monkey-patched instance is to give you the flexibility that the Selenium library already gives you, while giving you a shortcut for giving you what you want most of the time. For instance, you can check to make sure that an element is visible and then get the value.
```python
    assert login_page.username.is_displayed()
    assert login_page.username.value() == 'mmario'
```
