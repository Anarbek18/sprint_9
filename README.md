# Sprint_9: автотесты «Продуктового помощника»

Selenium + pytest + Allure, Page Object, запуск через Selenoid в Docker Compose.

## Локально
```
pip install -r requirements.txt
BASE_URL=https://<адрес сервиса> pytest
allure generate allure_results -o allure_report --clean
```

## Docker Compose + Selenoid
```
docker pull selenoid/chrome:128.0
BASE_URL=https://<адрес сервиса> docker compose up --build --abort-on-container-exit --exit-code-from tests
```

## CI/CD
Переменная `BASE_URL` (адрес сервиса, с `https://`). По умолчанию в CI: https://foodgram-frontend-1.foodgram.education-services.ru. Чтобы переопределить:
- GitHub: Settings → Secrets and variables → Actions → **Variables** → `BASE_URL`
- GitLab: Settings → CI/CD → **Variables** → `BASE_URL`

Пайплайны: `.github/workflows/ci.yml` и `.gitlab-ci.yml`. Отчёт Allure сохраняется как артефакт `allure_results`.
тест
