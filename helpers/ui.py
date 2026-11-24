import allure

import data
from pages.create_recipe_page import CreateRecipePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.step("Авторизоваться и перейти на главную страницу")
def login_and_get_main_page(driver, user):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(user)
    return MainPage(driver)


@allure.step("Создать рецепт с именем «{recipe_name}»")
def create_recipe(driver, main_page, recipe_name):
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
