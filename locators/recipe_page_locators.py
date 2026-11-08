from selenium.webdriver.common.by import By


class RecipePageLocators:
    RECIPE_CARD = (By.XPATH, "//div[contains(@class,'single-card')]")
    RECIPE_TITLE = (By.XPATH, "//h1")
