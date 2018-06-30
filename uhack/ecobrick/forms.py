from django.contrib.auth.models import User, Group
from django.forms import modelformset_factory
from django.db.models import Q
from .models import *

from django import forms
class login(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username','password']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password...'}),
        }


class register(forms.ModelForm):

    class Meta:

        model = UserDetail
        fields = ['username','password','email','firstName','lastName','address','contactNum']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password...'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail...'}),
            'firstName': forms.TextInput(attrs={'placeholder': 'First Name...'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Last Name...'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address...'}),
            'contactNum': forms.TextInput(attrs={'placeholder': 'Contact Number...'}),
            
        }
        
