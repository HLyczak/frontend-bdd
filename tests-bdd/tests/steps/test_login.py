import pytest
from pages.login_page import LoginPage
from pytest_bdd import given, parsers, scenarios, then, when
from selenium.webdriver.remote.webdriver import WebDriver
from utils.browser import wait_for_page_load

scenarios("../features/login.feature")


@pytest.fixture
def login_page(browser: WebDriver) -> LoginPage:
    return LoginPage(browser)


@given("I am on the login page")
def open_login_page(browser: WebDriver) -> None:
    browser.get(
        "http://www.automationpractice.pl/index.php?controller=authentication&back=my-account"
    )
    wait_for_page_load(browser)


@when(parsers.parse('I enter an invalid email "{email}"'))
def enter_invalid_email(login_page: LoginPage, email: str) -> None:
    login_page.enter_email(email)


@when(parsers.parse('I enter an invalid password "{password}"'))
def enter_invalid_password(login_page: LoginPage, password: str) -> None:
    login_page.enter_password(password)


@when("I click the login button")
def click_login_button(login_page: LoginPage) -> None:
    login_page.click_login()


@then(parsers.parse('I should see an error message "{message}"'))
def verify_error_message(login_page: LoginPage, message: str) -> None:
    error_message = login_page.get_error_message()
    assert (
        message in error_message
    ), f"❌ Expected error message '{message}', but got '{error_message}'"
