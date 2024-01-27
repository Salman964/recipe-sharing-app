# interaction/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Like, Comment, UserRating, FavoriteRecipe
from core.models import Recipe

@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    # Check if the user has already liked the recipe
    existing_like = Like.objects.filter(user=request.user, recipe=recipe).exists()

    if not existing_like:
        # Create a new like
        Like.objects.create(user=request.user, recipe=recipe)

    # Redirect to the recipe detail page
    return redirect('core:recipe_detail', recipe_id=recipe.id)

@login_required
def comment_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        # Create a new comment
        Comment.objects.create(user=request.user, recipe=recipe, text=text)

    # Redirect to the recipe detail page
    return redirect('core:recipe_detail', recipe_id=recipe.id)

@login_required
def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        # Create a new user rating
        UserRating.objects.create(user=request.user, recipe=recipe, rating=rating)

    # Redirect to the recipe detail page
    return redirect('core:recipe_detail', recipe_id=recipe.id)

@login_required
def favorite_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Check if the user has already favorited the recipe
    existing_favorite = FavoriteRecipe.objects.filter(user=request.user, recipe=recipe).exists()

    if not existing_favorite:
        # Create a new favorite
        FavoriteRecipe.objects.create(user=request.user, recipe=recipe)

    # Redirect to the recipe detail page
    return redirect('core:recipe_detail', recipe_id=recipe.id)
