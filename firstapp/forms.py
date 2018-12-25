from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",required=False, min_length=2, max_length=20)
    name2 = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    age = forms.IntegerField(label="Возраст")