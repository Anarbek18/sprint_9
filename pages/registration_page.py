import allure

import config
from locators.registration_page_locators import RegistrationPageLocators as Locators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    @allure.step("Открыть страницу регистрации")
    def open_page(self):
        self.open(config.SIGNUP_URL)

    @allure.step("Заполнить форму регистрации и отправить")
    def register(self, user):
        self.type_text(Locators.FIRST_NAME_INPUT, user["first_name"])
        self.type_text(Locators.LAST_NAME_INPUT, user["last_name"])
        self.type_text(Locators.USERNAME_INPUT, user["username"])
        self.type_text(Locators.EMAIL_INPUT, user["email"])
        self.type_text(Locators.PASSWORD_INPUT, user["password"])
        self.click(Locators.SUBMIT_BUTTON)
