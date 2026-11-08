import uuid
from pathlib import Path

RECIPE_IMAGE_PATH = str(Path(__file__).parent / "resources" / "recipe.png")

INGREDIENT_PREFIX = "мука"
INGREDIENT_AMOUNT = "100"
RECIPE_COOKING_TIME = "30"
RECIPE_DESCRIPTION = "Смешать ингредиенты и запечь до готовности."
RECIPE_TAG = "Завтрак"


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
