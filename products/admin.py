from django.contrib import admin



# Register your models here.
from .models import Product, ProductVariations, Category

#
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('product_name','price')
#
    list_display = ['product_name','price']

    class Meta:
        model = Product


class ProductVariationsAdmin(admin.ModelAdmin):
    search_fields = ('product_type','var_name')
    list_display = ['product_type','var_name']

    class Meta:
        model = ProductVariations


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductVariations)

