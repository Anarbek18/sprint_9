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
