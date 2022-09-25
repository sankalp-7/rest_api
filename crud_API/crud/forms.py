from django import forms
from . import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    #basic user creation form
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user