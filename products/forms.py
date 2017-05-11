from __future__ import unicode_literals

from django import forms

from products.models import Product, Category, ProductVariations, ProductImage


class ProductForm(forms.Model):
    class Meta:
        product_name = forms.CharField(max_length=100)
        price = forms.IntegerField()
        quantity = forms.CharField(max_length=20)
        category = forms.ForeignKey(Category)
        image = forms.ImageField(upload_to='media/products', default=1)


class ProductCreateForm(forms.Model):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'quantity', 'category', 'image']


class ProductListViewForm(forms.ModelForm):
    class Meta:
        model = Product


class ProductImageForm(forms.Model):
    class Meta:
        product_id = forms.ForeignKey(Product)
        img = forms.ImageField()


class CreateProductImageForm(forms.Model):
    class Meta:
        model = ProductImage
        fields = ['product_id', 'img']


class ProductImageListForm(forms.Model):
    class Meta:
        model = ProductImage


class CategoryForm(forms.ModelForm):
    class Meta:
        category_name = forms.CharField(max_length=100)


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class CategoryListViewForm(forms.ModelForm):
    class Meta:
        model = Category


class ProductVariationsForm(forms.ModelForm):
    class Meta:
        product_type = forms.ForeignKey(Product)
        variation_name = forms.CharField(max_length=100)
        sale_prices = forms.IntegerField()
        price = forms.IntegerField()


class CreateProductVariationsForm(forms.ModelForm):
    class Meta:
        model = ProductVariations
        fields = ['product_type', 'variation_name', ' sale_prices', ' price']


class ProductVariationsListViewForm(forms.ModelForm):
    class Meta:
        model = ProductVariations