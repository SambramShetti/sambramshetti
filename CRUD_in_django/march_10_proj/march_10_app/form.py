from django import forms
from .models import Product

class ItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_name', 'price', 'discount_price', 'category', 'description', 'image']
