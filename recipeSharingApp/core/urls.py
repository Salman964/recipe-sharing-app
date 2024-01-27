# core/urls.py
from django.shortcuts import redirect
from django.urls import path
from .views import recipe_list, recipe_detail, create_recipe, available_recipies,contact
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/contact', contact, name= 'contact'),
    path('recipes/available_recipies', available_recipies, name='available_recipies'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipes/create/', create_recipe, name='create_recipe'),
]
