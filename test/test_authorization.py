import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.title("После авторизации происходит переход на главную страницу")
    def test_login_redirects_to_main_page(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login(registered_user)

        assert MainPage(driver).is_main_page_opened()

    @allure.title("После авторизации отображается кнопка «Выход»")
    def test_login_shows_logout_button(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login(registered_user)

        assert MainPage(driver).is_logout_button_displayed()
