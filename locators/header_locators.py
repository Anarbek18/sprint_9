from selenium.webdriver.common.by import By


class HeaderLocators:
    SIGNUP_LINK = (By.XPATH, "//a[text()='Создать аккаунт']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[text()='Создать рецепт']")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Выход']")
