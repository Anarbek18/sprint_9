import allure
from selenium.webdriver.support.ui import WebDriverWait

import config
from locators.login_page_locators import LoginPageLocators as Locators
from pages.base_page import BasePage, TIMEOUT


class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_page(self):
        self.open(config.LOGIN_URL)

    @allure.step("Заполнить форму авторизации и отправить")
    def login(self, user):
        self.type_text(Locators.EMAIL_INPUT, user["email"])
        self.type_text(Locators.PASSWORD_INPUT, user["password"])
        # Wait until the submit button is enabled (React form validation)
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: d.find_element(*Locators.SUBMIT_BUTTON).is_enabled()
        )
        self.click(Locators.SUBMIT_BUTTON)
        # Give the app time to process login and redirect
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda d: "signin" not in d.current_url
        )

    def is_login_page_opened(self):
        return self.is_url_equal(config.LOGIN_URL)

    def is_login_form_displayed(self):
        return self.is_visible(Locators.LOGIN_FORM)
