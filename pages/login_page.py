import allure

import config
from locators.login_page_locators import LoginPageLocators as Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_page(self):
        self.open(config.LOGIN_URL)

    @allure.step("Заполнить форму авторизации и отправить")
    def login(self, user):
        self.type_text(Locators.EMAIL_INPUT, user["email"])
        self.type_text(Locators.PASSWORD_INPUT, user["password"])
        self.click(Locators.SUBMIT_BUTTON)

    def is_login_page_opened(self):
        return self.is_url_equal(config.LOGIN_URL)

    def is_login_form_displayed(self):
        return self.is_visible(Locators.LOGIN_FORM)
