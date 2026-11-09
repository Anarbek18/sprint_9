import pytest
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector

import config
import data
from helpers import api
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    if config.SELENIUM_URL:
        browser = webdriver.Remote(command_executor=config.SELENIUM_URL, options=options)
        browser.file_detector = LocalFileDetector()
    else:
        browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user():
    return api.create_user(data.generate_user())


@pytest.fixture
def new_user():
    return data.generate_user()


@pytest.fixture
def logged_in_main_page(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(registered_user)
    main_page = MainPage(driver)
    main_page.is_logout_button_displayed()
    return main_page
