from django import forms
from django.contrib.auth import get_user_model
from .models import UserInformation

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

    def clean_username(self):
        profile = self.cleaned_data.get('username')
        queryset = User.objects.filter(username__iexact=profile)

        if not queryset.exists():
            raise forms.ValidationError("Wrong username or password")

        return profile

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

    def clean_username(self):
        profile = self.cleaned_data.get("username")
        queryset = User.objects.filter(username__iexact=profile)

        if queryset.exists():
            raise forms.ValidationError("Invalid username")

        return profile

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = [
            'bio', 
            'profile_image',
        ]