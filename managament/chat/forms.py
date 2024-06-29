from django import forms
from .models import Chat
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message', 'photo']
        

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email address', required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']