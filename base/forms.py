from django.forms import ModelForm
from django import forms
from .models import Contact
from django.core.validators import validate_email


class PostForm(ModelForm):
     
    class Meta:
        model = Contact
        fields = ('name', 'email','message')       
 
     