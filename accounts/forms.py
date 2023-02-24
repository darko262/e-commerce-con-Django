from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class LoginForm(forms.ModelForm):
    class Meta:
        model=Account
        fields = ['first_name','password']

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Ingrese Password', 'class': 'form-control',
        }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Confirmar Password','class': 'form-control',
        }))
    class Meta:
        model= Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']
    pass

class AutenticarForm(AuthenticationForm):
    pass

