from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegistrationPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.email_input: tuple = (By.ID, "email_create")
        self.create_account_button: tuple = (By.ID, "SubmitCreate")
        self.first_name_input: tuple = (By.ID, "customer_firstname")
        self.last_name_input: tuple = (By.ID, "customer_lastname")
        self.password_input: tuple = (By.ID, "passwd")
        self.submit_button: tuple = (By.ID, "submitAccount")
        self.error_message_empty_form_fields: tuple = (By.CSS_SELECTOR, ".alert-danger")
        self.error_message_invalid_email: tuple = (By.ID, "create_account_error")
        self.success_message: tuple = (
            By.XPATH,
            "//p[contains(@class, 'alert-success')]",
        )

    def enter_email(self, email: str) -> None:
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_create_account(self) -> None:
        self.driver.find_element(*self.create_account_button).click()

    def fill_registration_form(
        self, first_name: str, last_name: str, password: str
    ) -> None:
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit_registration(self) -> None:
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self) -> str:
        return self.driver.find_element(*self.success_message).text

    def get_error(self) -> str:
        return self.driver.find_element(*self.error_message_empty_form_fields).text
