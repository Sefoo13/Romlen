from django import forms
from django.contrib.auth.models import User
from firstapp.models import Company
from django.contrib.auth.forms import UserCreationForm


class CompanyForm(UserCreationForm):
    name = forms.CharField()

    class Meta:
        model = User
        fields = ('name', 'username', 'password1', 'password2')


class CompanyEditForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name',)