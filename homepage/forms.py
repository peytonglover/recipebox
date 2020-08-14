from django import forms
from homepage.models import Recipe, Author

class AddRecipeForm(forms.Form):
    title=forms.CharField(max_length=50)
    description= forms.CharField(widget=forms.Textarea)
    timerequired=forms.CharField(max_length=50)
    instructions=forms.CharField(widget=forms.Textarea)
    
class AddAuthorForm(forms.ModelForm):
    # name=forms.CharField(max_length=50)
    # bio=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Author
        fields = ['name', 'bio']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)