from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import SchoolOwner, Comment, Contend

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')
    
class SchoolForms(forms.ModelForm):
    class Meta:
        model=SchoolOwner
        fields=('schoolname','phone','address')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ContendForm(ModelForm):
    class Meta:
        model = Contend
        fields = ('name', 'email', 'text')