from django import forms
from homepage.models import Recipe, Author

class RecipeForm(forms.Form):
    title=forms.CharField(max_length=50)
    author= forms.ModelChoiceField(queryset=Author.objects.all())
    description= forms.CharField(widget=forms.Textarea)
    timerequired=forms.CharField(max_length=50)
    instructions=forms.CharField(widget=forms.Textarea)
    
class AuthorForm(forms.ModelForm):
    # name=forms.CharField(max_length=50)
    # bio=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Author
        fields = ['name', 'bio']
