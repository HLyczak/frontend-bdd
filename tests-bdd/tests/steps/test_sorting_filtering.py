import pytest
from pages.sorting_filtering_page import SortingFilteringPage
from pytest_bdd import given, parsers, scenarios, then, when
from utils.browser import wait_for_page_load

scenarios("../features/sorting_filtering.feature")


@pytest.fixture
def sorting_filtering_page(browser):
    return SortingFilteringPage(browser)


@given("I am on the shop page")
def open_shop_page(browser):
    browser.get(
        "http://automationpractice.pl/index.php?id_category=3&controller=category"
    )
    wait_for_page_load(browser)


@when(parsers.parse('I sort items by "{sort_option}"'))
def sort_items(sorting_filtering_page, sort_option):
    sorting_filtering_page.sort_items(sort_option)


@then("I should see items sorted by price")
def verify_sorted_items(sorting_filtering_page):
    assert sorting_filtering_page.is_sorted_correctly()


@when(parsers.parse('I filter items by category "{category}"'))
def filter_items_by_category(sorting_filtering_page, category):
    sorting_filtering_page.filter_by_category(category)


@then("I should see only dresses")
def verify_filtered_items(sorting_filtering_page):
    assert (
        sorting_filtering_page.is_filtered_correctly()
    ), "Filtering by category failed"
