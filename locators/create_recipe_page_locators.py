from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    TAG_LABEL = "//label[contains(., '{}')]"
    INGREDIENT_INPUT = (By.XPATH, "//input[@name='nameIngredient' or @placeholder='Ингредиенты']")
    INGREDIENT_OPTION = (By.XPATH, "(//div[contains(@class,'ingredients')]//div[contains(@class,'container')]/div)[1]")
    AMOUNT_INPUT = (By.XPATH, "//input[@name='value' or @placeholder='Количество']")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//*[text()='Добавить ингредиент']")
    COOKING_TIME_INPUT = (By.XPATH, "//input[@name='cookingTime']")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description']")
    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
