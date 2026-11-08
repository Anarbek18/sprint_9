import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.header_locators import HeaderLocators

TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        self.wait_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    def is_url_matching(self, pattern):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.url_matches(pattern))
            return True
        except Exception:
            return False

    def is_url_equal(self, url):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.url_to_be(url))
            return True
        except Exception:
            return False

    @allure.step("Нажать «Создать аккаунт» в шапке")
    def click_signup_link(self):
        self.click(HeaderLocators.SIGNUP_LINK)

    @allure.step("Нажать «Войти» в шапке")
    def click_login_link(self):
        self.click(HeaderLocators.LOGIN_LINK)
