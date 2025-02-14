import pytest
from pages.shopping_page import ShoppingPage
from pytest_bdd import given, parsers, scenarios, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.browser import wait_for_page_load

scenarios("../features/shopping_flow.feature")


@pytest.fixture
def shopping_page(browser: WebDriver) -> ShoppingPage:
    return ShoppingPage(browser)


@given("I am on the home page")
def open_home_page(browser: WebDriver) -> None:
    browser.get("http://automationpractice.pl/index.php")
    wait_for_page_load(browser)


@when(parsers.parse('I search for an item "{item}"'))
def search_for_item(shopping_page: ShoppingPage, item: str) -> None:
    shopping_page.search_for_item(item)


@when("I attempt to add the first item to the cart")
def attempt_add_item_to_cart(shopping_page: ShoppingPage) -> None:
    shopping_page.add_first_item_to_cart()


@then("I should see an out-of-stock alert")
def verify_out_of_stock_alert(shopping_page: ShoppingPage) -> None:

    close_button = WebDriverWait(shopping_page.browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fancybox-close"))
    )
    close_button.click()
    alert = WebDriverWait(shopping_page.browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(@id, 'availability_value')]")
        )
    )
    alert_text = alert.text.strip()

    assert (
        "This product is no longer in stock with those attributes but is available with others."
        in alert_text
    ), "Expected out-of-stock message, but it was not found!"


@when("I go to the cart page")
def go_to_cart(shopping_page: ShoppingPage) -> None:
    shopping_page.go_to_cart()


@then("my cart should be empty")
def verify_cart_empty(shopping_page: ShoppingPage) -> None:
    assert shopping_page.is_cart_empty(), "Cart is not empty!"
