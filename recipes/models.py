from django.db import models
from django.utils import timezone

# Create your models here.
difficulty_choices = (
    ("Easy", "easy"),
    ("Medium", "medium"),
    ("Intermediate", "intermediate"),
    ("Hard", "hard"),
)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cooking_time = models.IntegerField(
        help_text="Enter the cooking time in minutes", default=0
    )
    ingredients = models.CharField(
        max_length=250, help_text="Enter each ingredient separated by a comma"
    )
    difficulty = models.CharField(
        max_length=120, choices=difficulty_choices, default="Easy"
    )
    pic = models.ImageField(
        upload_to="recipes",
        help_text="Upload Image (Min.250px)",
        default="no_picture.jpg",
    )
    author = models.CharField(max_length=120, default="anonymous")
    instructions = models.TextField(default="No instructions ...")
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.difficulty} - {self.cooking_time}"

    def save(self, *args, **kwargs):
        self.calc_difficulty()
        super().save(*args, **kwargs)

    def calc_difficulty(self):
        ingredients_len = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and ingredients_len < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len >= 4:
            self.difficulty = "Hard"
