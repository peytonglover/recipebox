from django.shortcuts import render
from homepage.models import Recipe, Author

# Create your views here.
def simplelist(request):
    my_recipes = Recipe.objects.all()
    return render(request, 'simplelist.html', {"recipes": my_recipes, "name": "bob"})

def recipedetail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipedetail.html', {"recipe": my_recipe})

def authordetail(request, author_name):
    recipes = Recipe.objects.all()
    my_author = Author.objects.filter(name=author_name).first()
    return render(request, 'authordetail.html', {"author": my_author, "recipes": recipes})