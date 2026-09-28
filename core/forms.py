from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'input-area',
        'placeholder' : 'your username',
    }) )

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'input-area',
        'placeholder' : 'your email',
    }) )

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input-area',
        'placeholder' : 'your password',
    }) )

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input-area',
        'placeholder' : 'repeat password',
    }) )

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'input-area',
        'placeholder' : 'your username',
    }) )

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input-area',
        'placeholder' : 'your password',
    }) )