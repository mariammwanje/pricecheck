from django.contrib import admin

from products.models import Product, Category, ProductVariations

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductVariations)
# admin.site.register(ProductImage)
