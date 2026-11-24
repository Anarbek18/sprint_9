import allure
import re

import config
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_page(self):
        self.open(config.BASE_URL)

    def is_main_page_opened(self):
        # Match main page or recipes list (with or without trailing slash)
        pattern = r"^" + re.escape(config.BASE_URL) + r"/(recipes/?)?$"
        return self.is_url_matching(pattern)

    def is_logout_button_displayed(self):
        return self.is_visible(HeaderLocators.LOGOUT_LINK)

    @allure.step("Перейти на таб «Создать рецепт»")
    def go_to_create_recipe(self):
        self.click(HeaderLocators.CREATE_RECIPE_LINK)
