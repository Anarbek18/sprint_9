import os

# Адрес тестируемого сервиса «Продуктовый помощник»
BASE_URL = os.getenv("BASE_URL", "https://foodgram-your-domain.example").rstrip("/")
# Адрес Selenoid. Если не задан, тесты запускаются в локальном Chrome
SELENIUM_URL = os.getenv("SELENIUM_URL")

SIGNUP_URL = f"{BASE_URL}/signup"
LOGIN_URL = f"{BASE_URL}/signin"
CREATE_RECIPE_URL = f"{BASE_URL}/recipes/create"
MAIN_URL_PATTERN = r"/(recipes/?)?$"

API_USERS = f"{BASE_URL}/api/users/"
