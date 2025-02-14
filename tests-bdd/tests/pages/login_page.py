from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "passwd")
        self.login_button = (By.ID, "SubmitLogin")
        self.error_message = (By.XPATH, "//div[contains(@class, 'alert-danger')]")
        self.account_section = (By.CLASS_NAME, "account")

    def enter_email(self, email: str) -> None:
        self.browser.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password: str) -> None:
        self.browser.find_element(*self.password_input).send_keys(password)

    def click_login(self) -> None:
        self.browser.find_element(*self.login_button).click()

    def is_logged_in(self) -> bool:
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.account_section)
            )
            return True
        except:
            return False

    def get_error_message(self) -> str:
        try:
            return self.browser.find_element(*self.error_message).text.strip()
        except:
            return ""
