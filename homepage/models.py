from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Author:
# name (80 characters)
# bio (textfield)

# Recipe:
# title (50 characters)
# author(foreign key)
# description(textfield)
# time required(charfield)
# instructions(textfield)

class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    timerequired = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"
        ## the f string is adding author name to the recipe the curly brackets are holders for "variables"
        