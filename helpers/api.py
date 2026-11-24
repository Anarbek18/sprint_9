import allure
import requests

import config
from helpers import generators


@allure.step("Создать пользователя через API")
def create_user(user):
    response = requests.post(config.API_USERS, json=user)
    response.raise_for_status()
    return user


@allure.step("Зарегистрировать нового пользователя через API")
def register_new_user():
    return create_user(generators.generate_user())
