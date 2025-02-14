from behave.runner import Context
from utils.browser import get_driver


def before_all(context: Context) -> None:
    context.driver = get_driver()


def after_all(context: Context) -> None:
    context.driver.quit()
