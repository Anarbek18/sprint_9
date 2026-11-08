import allure
from selenium.webdriver.common.by import By

from locators.create_recipe_page_locators import CreateRecipePageLocators as Locators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):
    @allure.step("Выбрать тег рецепта")
    def select_tag(self, tag):
        self.click((By.XPATH, Locators.TAG_LABEL.format(tag)))

    @allure.step("Добавить ингредиент из выпадающего списка")
    def add_ingredient(self, name_prefix, amount):
        self.type_text(Locators.INGREDIENT_INPUT, name_prefix)
        self.click(Locators.INGREDIENT_OPTION)
        self.type_text(Locators.AMOUNT_INPUT, amount)
        self.click(Locators.ADD_INGREDIENT_BUTTON)

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, path):
        self.driver.find_element(*Locators.IMAGE_INPUT).send_keys(path)

    @allure.step("Заполнить форму создания рецепта и отправить")
    def create_recipe(self, name, tag, ingredient_prefix, amount, cooking_time, description, image_path):
        self.type_text(Locators.NAME_INPUT, name)
        self.select_tag(tag)
        self.add_ingredient(ingredient_prefix, amount)
        self.type_text(Locators.COOKING_TIME_INPUT, cooking_time)
        self.type_text(Locators.DESCRIPTION_TEXTAREA, description)
        self.upload_image(image_path)
        self.click(Locators.SUBMIT_BUTTON)
