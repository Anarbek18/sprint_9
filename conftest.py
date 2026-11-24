import pytest
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector

import config


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
