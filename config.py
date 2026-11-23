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

# Адрес API. По умолчанию выводится из BASE_URL заменой поддомена
# frontend на backend, но можно переопределить переменной окружения API_URL.
API_URL = os.getenv("API_URL", "").strip().rstrip("/")
if not API_URL:
    API_URL = BASE_URL.replace("frontend", "backend", 1)
if not API_URL.startswith(("http://", "https://")):
    raise RuntimeError(
        "Переменная окружения API_URL задана без http(s)://. "
        "Укажите адрес API, например https://my-foodgram-backend.example"
    )

API_USERS = f"{API_URL}/api/users/"
