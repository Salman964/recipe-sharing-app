# core/views.py
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeImageFormSet
from django.contrib import messages 

from django.contrib.auth.models import User
import pdb

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'core/recipe_list.html', {'recipes': recipes})

def contact(request):
    return render(request, 'core/contact.html')


def available_recipies(request):
    recipes = Recipe.objects.all()
    return render(request, 'core/available_recipies.html', {'recipes': recipes})

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        formset = RecipeImageFormSet(request.POST, request.FILES, prefix='images')

        if form.is_valid() and formset.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = User.objects.first()
            new_recipe.save()

            # Associate the new_recipe with the images
            formset.instance = new_recipe
            formset.save()

            messages.success(request, 'Recipe created successfully!')
            return redirect('core:recipe_detail', recipe_id=new_recipe.id)

    else:
        form = RecipeForm()
        formset = RecipeImageFormSet(prefix='images')

    return render(request, 'core/create_recipe.html', {'form': form, 'formset': formset})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'core/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'core/recipe_detail.html', {'recipe': recipe})
