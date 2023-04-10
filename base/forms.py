from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task

class TaskForms(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'title',
            'description',
            'completed',
        ]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']