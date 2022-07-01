from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        modal = User
        field = ['username', 'password1', 'password2']
