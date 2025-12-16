from django import forms
from .models import AcessRequest, SourceChoices, StatusChoices
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class AcessRequestForm(forms.ModelForm):
    class Meta:
        model = AcessRequest
        fields = ['source', 'reason']
        widgets = {
            'source': forms.Select(choices=SourceChoices.choices),
            'reason': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'source': 'Source',
            'reason': 'Reason',
        }
class AcessRequestAdminForm(forms.ModelForm):
    class Meta:
        model = AcessRequest
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=StatusChoices.choices),
        }
        labels = {
            'status': 'Status',
        }