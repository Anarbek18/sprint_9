import os

# Адрес тестируемого сервиса «Продуктовый помощник».
# Обязательная переменная окружения BASE_URL, например https://my-foodgram.example
BASE_URL = os.getenv("BASE_URL", "").strip().rstrip("/")
if not BASE_URL.startswith(("http://", "https://")):
    raise RuntimeError(
        "Переменная окружения BASE_URL не задана или задана без http(s)://. "
        "Укажите адрес сервиса: GitHub — Settings → Secrets and variables → Actions → Variables; "
        "GitLab — Settings → CI/CD → Variables."
    )

# Адрес Selenoid. Если не задан, тесты запускаются в локальном Chrome
SELENIUM_URL = os.getenv("SELENIUM_URL")

SIGNUP_URL = f"{BASE_URL}/signup"
LOGIN_URL = f"{BASE_URL}/signin"
CREATE_RECIPE_URL = f"{BASE_URL}/recipes/create"
MAIN_URL_PATTERN = r"/(recipes/?)?$"

API_USERS = f"{BASE_URL}/api/users/"
