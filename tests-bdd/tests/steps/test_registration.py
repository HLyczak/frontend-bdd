import time

import pytest
from pages.registration_page import RegistrationPage
from pytest_bdd import given, parsers, scenarios, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

scenarios("../features/registration_senario.feature")


@pytest.fixture
def registration_page(browser: WebDriver) -> RegistrationPage:
    return RegistrationPage(browser)


@given("I am on the registration page")
def open_registration_page(browser: WebDriver) -> None:
    browser.get(
        "http://www.automationpractice.pl/index.php?controller=authentication&back=my-account"
    )
    WebDriverWait(browser, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "email_create"))
    )


@when(parsers.parse("I enter a valid email {email}"))
def enter_valid_email(registration_page: RegistrationPage, email: str) -> None:
    timestamp: int = int(time.time())
    email_with_timestamp: str = (
        f"{email.split('@')[0]}_{timestamp}@{email.split('@')[1]}"
    )

    registration_page.enter_email(email_with_timestamp)
    registration_page.click_create_account()

    WebDriverWait(registration_page.driver, 10).until(
        EC.presence_of_element_located((By.ID, "account-creation_form"))
    )


@when(parsers.parse("I enter an invalid email {email}"))
def enter_invalid_email(registration_page: RegistrationPage, email: str) -> None:
    registration_page.enter_email(email)
    registration_page.click_create_account()

    WebDriverWait(registration_page.driver, 10).until(
        EC.presence_of_element_located((By.ID, "create_account_error"))
    )


@when("I fill in the registration form with valid details")
def fill_registration_form(registration_page: RegistrationPage) -> None:
    registration_page.fill_registration_form("John", "Doe", "SecurePass123")


@when("I submit the form")
def submit_form(registration_page: RegistrationPage) -> None:
    registration_page.submit_registration()
    WebDriverWait(registration_page.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
    )


@when("I submit the form without filling required fields")
def submit_empty_form(registration_page: RegistrationPage) -> None:
    registration_page.submit_registration()
    WebDriverWait(registration_page.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
    )


@then(parsers.parse("I should see a confirmation message {message}"))
def verify_success_message(registration_page: RegistrationPage, message: str) -> None:
    success_message: str = registration_page.get_success_message()
    assert message in success_message, f"Expected '{message}', got '{success_message}'"


@then("I should see error messages for the missing fields")
def verify_missing_fields_error(registration_page: RegistrationPage) -> None:
    WebDriverWait(registration_page.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
    )
    error_messages: str = registration_page.get_error()
    assert len(error_messages) > 0, "Expected missing field errors, but found none"
