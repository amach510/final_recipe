from django.urls import path
from .views import home, RecipesListView, RecipesDetailView

app_name = "recipes"

urlpatterns = [
    path("", home, name="home"),
    path("recipes/", RecipesListView.as_view(), name="recipes"),
    path("recipes/<pk>", RecipesDetailView.as_view(), name="detail"),
]
