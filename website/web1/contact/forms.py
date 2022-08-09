from attr import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 
from .models import contact 
from .models import * 
from .forms import CreateUserForm

class contact(ModelForm):
    class Meta:
        model = contact 
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username' ,'email' ,'password' ,'password2']