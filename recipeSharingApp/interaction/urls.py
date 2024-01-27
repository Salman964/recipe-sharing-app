# interaction/urls.py
from django.urls import path
from .views import like_recipe, comment_recipe, rate_recipe, favorite_recipe

app_name = 'interaction'

urlpatterns = [
    path('like/<int:recipe_id>/', like_recipe, name='like_recipe'),
    path('comment/<int:recipe_id>/', comment_recipe, name='comment_recipe'),
    path('rate/<int:recipe_id>/', rate_recipe, name='rate_recipe'),
    path('favorite/<int:recipe_id>/', favorite_recipe, name='favorite_recipe'),
]
