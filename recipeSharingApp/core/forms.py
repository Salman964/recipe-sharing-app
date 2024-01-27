# core/forms.py
from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions']

    # Modify the widget for multiline text input
    widgets = {
        'ingredients': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        'instructions': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
    }

RecipeImageFormSet = forms.inlineformset_factory(Recipe, RecipeImage, fields=['image'], extra=1)
