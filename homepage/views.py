from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from homepage.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
                title=data.get('title'),
                author=request.user.author,
                description=data.get('description'),
                timerequired=data.get('timerequired'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse('recipedetail', args=[new_recipe.id]))
    form = AddRecipeForm()
    return render(request, 'forms.html', {'form': form})

@login_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    if request.user.is_staff:
        form = AddAuthorForm()
        return render(request, 'forms.html', {'form': form})


def loginform(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'forms.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #actually creating the user..
            new_user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
            Author.objects.create(name=data.get('username'), user=new_user)
            #to log in the user after they create..
            login(request, new_user)
            #redirecting to homepage after they create..
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'forms.html', {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
