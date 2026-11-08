import allure

import data
from pages.create_recipe_page import CreateRecipePage
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestCreateRecipe:
    @staticmethod
    def _create_recipe(driver, main_page, recipe_name):
        main_page.go_to_create_recipe()
        CreateRecipePage(driver).create_recipe(
            name=recipe_name,
            tag=data.RECIPE_TAG,
            ingredient_prefix=data.INGREDIENT_PREFIX,
            amount=data.INGREDIENT_AMOUNT,
            cooking_time=data.RECIPE_COOKING_TIME,
            description=data.RECIPE_DESCRIPTION,
            image_path=data.RECIPE_IMAGE_PATH,
        )

    @allure.title("После создания рецепта отображается его карточка")
    def test_created_recipe_card_is_displayed(self, driver, logged_in_main_page):
        self._create_recipe(driver, logged_in_main_page, data.generate_recipe_name())

        assert RecipePage(driver).is_recipe_card_displayed()

    @allure.title("В карточке рецепта отображается название, указанное при создании")
    def test_created_recipe_has_entered_name(self, driver, logged_in_main_page):
        recipe_name = data.generate_recipe_name()
        self._create_recipe(driver, logged_in_main_page, recipe_name)

        assert RecipePage(driver).get_recipe_title() == recipe_name
