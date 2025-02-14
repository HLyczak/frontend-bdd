import pytest
from utils.browser import get_browser


@pytest.fixture
def browser():
    driver = get_browser()
    yield driver
    driver.quit()
