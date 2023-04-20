from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, max_length=30)
    password2 = forms.CharField(required=True, max_length=30)    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")
