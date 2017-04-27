# Selenium Page Elements

Selenium Page Elements aim to make Page Objects quick and easy by allowing you to define and interact with input fields like object attributes.

```python
# Page Object
from selenium.webdriver.common.by import By
from page_elements import InputField, CheckBox


class LoginPage:
    url = "http://localhost/login"

    # Define your elements in your class.
    username = InputField(By.ID, 'username')
    password = InputField(By.ID, 'password')
    stay_signed_in = CheckBox(By.ID, 'stay-signed-in')
    login_button = Button(By.ID, 'submit-login')

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


# Tests
from selenium import webdriver
from your.page_objects import LoginPage, HomePage


def test_successful_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        username='jsmith',
        password='hunter2',
        stay_signed_in=False)
    assert driver.current_page == HomePage.url
```
