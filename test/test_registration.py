import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("После регистрации происходит переход на страницу авторизации")
    def test_registration_redirects_to_login_page(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_signup_link()
        RegistrationPage(driver).register(new_user)

        assert LoginPage(driver).is_login_page_opened()

    @allure.title("После регистрации отображается форма авторизации")
    def test_registration_shows_login_form(self, driver, new_user):
        registration_page = RegistrationPage(driver)
        registration_page.open_page()
        registration_page.register(new_user)

        assert LoginPage(driver).is_login_form_displayed()
