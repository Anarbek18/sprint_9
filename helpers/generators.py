import uuid


def generate_user():
    suffix = uuid.uuid4().hex[:8]
    return {
        "first_name": "Иван",
        "last_name": "Тестов",
        "username": f"user_{suffix}",
        "email": f"user_{suffix}@example.com",
        "password": "Password123!",
    }


def generate_recipe_name():
    return f"Рецепт {uuid.uuid4().hex[:8]}"
