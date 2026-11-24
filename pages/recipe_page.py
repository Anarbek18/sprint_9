from locators.recipe_page_locators import RecipePageLocators as Locators
from pages.base_page import BasePage


class RecipePage(BasePage):
    def is_recipe_card_displayed(self):
        return self.is_visible(Locators.RECIPE_CARD)

    def get_recipe_title(self):
        return self.get_text(Locators.RECIPE_TITLE)
