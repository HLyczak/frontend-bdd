from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShoppingPage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser: WebDriver = browser

    def search_for_item(self, item: str) -> None:
        search_box = self.browser.find_element(By.ID, "search_query_top")
        search_box.clear()
        search_box.send_keys(item)
        search_box.submit()

    def add_first_item_to_cart(self) -> None:
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-container"))
        )
        first_item = self.browser.find_element(By.CLASS_NAME, "product-container")
        first_item.click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "add_to_cart"))
        )
        add_to_cart_button = self.browser.find_element(By.ID, "add_to_cart")
        add_to_cart_button.click()

    def is_out_of_stock_alert_present(self) -> bool:
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[contains(@id, 'availability_value')]")
                )
            )
            return True
        except:
            return False

    def go_to_cart(self) -> None:
        cart_button = self.browser.find_element(
            By.XPATH, "//a[contains(@title,'View my shopping cart')]"
        )
        cart_button.click()

    def is_cart_empty(self) -> bool:
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(@class,'alert-warning')]")
            )
        )
        return "Your shopping cart is empty" in self.browser.page_source
