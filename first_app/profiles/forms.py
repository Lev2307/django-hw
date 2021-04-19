from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Ваше имя'
                } 
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form_password',
                'placeholder': 'Пароль'
            }
        )
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Ваше имя'
                } 
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Ваша почта'
                } 
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form_password',
                'placeholder': 'Пароль'
            }
        )
    )