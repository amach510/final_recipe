from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe


# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Omelette",
            cooking_time=10,
            ingredients="Eggs, Butter, Salt, Pepper, Onion, Bell Pepper, Ham",
        )

    # Test for recipe name being initialized
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    # Test for recipe name exceeding 100 characters
    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 100, "name has over 100 characters")

    # Test for recipe cooking_time being an integer
    def test_cooking_time_is_integer(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertIs(type(cooking_time), int, "cooking_time is not a number")

    # Test for recipe ingredients exceeding 250 characters in ingredients field
    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 250, "ingredients has over 250 characters")

    # Test for recipe difficulty ensuring calculate_difficulty works
    def test_calculate_difficulty(self):
        recipe = Recipe(
            cooking_time=10,
            ingredients="Ingredient 1, Ingredient 2, Ingredient 3, Ingredient 4",
        )
        recipe.save()  # calls calc_difficulty
        self.assertEqual(recipe.difficulty, "Hard")

class RecipeAuthTest(TestCase):
    def setUpTestData():
        pass
