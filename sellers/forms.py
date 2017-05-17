
from __future__ import unicode_literals

from django import forms

from products.models import Product
from sellers.models import Seller


class SellerForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(max_length=100)
        contact = forms.IntegerField()
        address = forms.CharField(max_length=100)
        email = forms.EmailField()
        country = forms.CharField(max_length=100)
        contact_person = forms.CharField(max_length=100)
        seller_logo = forms.ImageField(upload_to='media/products')


class SellerProductForm(forms.ModelForm):
    class Meta:
        name_product = forms.ForeignKey(Product)
        seller_name = forms.ForeignKey(Seller)
        seller_price = forms.IntegerField()
        image = forms.ImageField(upload_to='media/products',  default=1)
