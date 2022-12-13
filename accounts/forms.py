from django import forms
from django.contrib.auth.models import User
from .models import School,Debtor,DebtInfo

class CreateUserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=('username','email','password')
        widgets = {
            'password': forms.PasswordInput() 
        }
    
class SchoolForms(forms.ModelForm):
    class Meta:
        model=School
        fields=('schoolname','phone','address')

class DebtorForms(forms.ModelForm):
    class Meta:
        model=Debtor
        fields=('guardian_name','full_name','school_name','level')


class DebtorInfoForm(forms.ModelForm):
    class Meta:
        model=DebtInfo
        fields='__all__'