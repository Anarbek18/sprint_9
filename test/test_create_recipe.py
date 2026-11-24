import allure

from helpers import generators, ui
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestCreateRecipe:
    @allure.title("После создания рецепта отображается его карточка")
    def test_created_recipe_card_is_displayed(self, driver, registered_user):
        main_page = ui.login_and_get_main_page(driver, registered_user)
        ui.create_recipe(driver, main_page, generators.generate_recipe_name())

        assert RecipePage(driver).is_recipe_card_displayed()

    @allure.title("В карточке рецепта отображается название, указанное при создании")
    def test_created_recipe_has_entered_name(self, driver, registered_user):
        recipe_name = generators.generate_recipe_name()
        main_page = ui.login_and_get_main_page(driver, registered_user)
        ui.create_recipe(driver, main_page, recipe_name)

        assert RecipePage(driver).get_recipe_title() == recipe_name
