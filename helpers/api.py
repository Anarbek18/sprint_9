import allure
import requests

import config


@allure.step("Создать пользователя через API")
def create_user(user):
    response = requests.post(config.API_USERS, json=user)
    response.raise_for_status()
    return user
