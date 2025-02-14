import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SortingFilteringPage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser: WebDriver = browser

    def sort_items(self, sort_option: str) -> None:
        sort_dropdown: WebElement = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "selectProductSort"))
        )
        sort_dropdown.click()
        self.browser.find_element(
            By.XPATH, f"//option[contains(text(), '{sort_option}')]"
        ).click()

    def is_sorted_correctly(self, descending: bool = False) -> bool:
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-price"))
        )
        time.sleep(2)

        price_elements: List[WebElement] = self.browser.find_elements(
            By.XPATH,
            "//span[contains(@class, 'product-price') and not(@itemprop) and not(contains(@class, 'old-price'))]",
        )

        prices: List[float] = [
            float(price.text.replace("$", "").strip())
            for price in price_elements
            if price.text.strip()
        ]

        return prices == sorted(prices, reverse=descending)

    def filter_by_category(self, category: str) -> None:
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, category))
        ).click()

    def is_filtered_correctly(self) -> bool:
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-container"))
        )
        products: List[WebElement] = self.browser.find_elements(
            By.CLASS_NAME, "product-container"
        )
        return len(products) > 0
