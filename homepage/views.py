from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm

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

def recipeform(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                timerequired=data.get('timerequired'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = RecipeForm()
    return render(request, 'forms.html', {'form': form})

def authorform(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = AuthorForm()
    return render(request, 'forms.html', {'form': form})
