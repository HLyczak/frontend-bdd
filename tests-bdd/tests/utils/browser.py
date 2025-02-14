from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def get_browser() -> WebDriver:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
        options=options,
    )
    driver.implicitly_wait(10)
    return driver


def wait_for_page_load(browser: WebDriver, timeout: int = 20) -> None:
    WebDriverWait(browser, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(("css selector", "body"))
    )
