from django import forms

from firstapp.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ('name', 'count')
        fields = ('company', 'name', 'count')
#