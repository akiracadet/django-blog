from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserModel

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=False)

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
