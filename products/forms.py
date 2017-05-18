from __future__ import unicode_literals

from django import forms

from products.models import Product, Category, ProductVariations, ProductImage


class ProductForm(forms.Model):
    class Meta:
        product_name = forms.CharField(max_length=100)
        price =forms.IntegerField()
        description = forms.TextField(max_length=500)
        # category = forms.ForeignKey(Category)
        image = forms.ImageField(upload_to='media/products')
        categories = forms.ManyToManyField(Category)
        default = forms.ForeignKey('Category', related_name='default_category', null=True, blank=False)
        active = forms.BooleanField(default=True)


class ProductCreateForm(forms.Model):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'categories', 'description', 'category', 'image','default','active']


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
        category_name = forms.CharField(max_length=100, unique=True)
        description = forms.TextField(null=True, blank=True)
        image = forms.ImageField(upload_to="media/category")
        active = forms.BooleanField(default=True)
        timestamp = forms.DateTimeField(auto_now_add=True, auto_now=False)


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'image', 'description','active','timestamp']

class CategoryListViewForm(forms.ModelForm):
    class Meta:
        model = Category


class ProductVariationsForm(forms.ModelForm):
    class Meta:
        product_type = forms.ForeignKey(Product)
        var_name = forms.CharField(max_length=100)
        var_price = forms.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
        sales_price = forms.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
        active = forms.BooleanField(default=True)


class CreateProductVariationsForm(forms.ModelForm):
    class Meta:
        model = ProductVariations
        fields = ['product_type', 'var_name', 'var_price',
                  ' sales_price', 'active']


class ProductVariationsListViewForm(forms.ModelForm):
    class Meta:
        model = ProductVariations
