from django import forms
from django.contrib.auth.models import User
from .models import SchoolOwner

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')
    
class SchoolForms(forms.ModelForm):
    class Meta:
        model=SchoolOwner
        fields=('schoolname','phone','address')