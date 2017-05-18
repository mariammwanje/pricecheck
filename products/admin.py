from django.contrib import admin

from products.models import Product, Category, ProductVariations

# Register your models here.


class ProductVariationsAdmin(admin.ModelAdmin):
    search_fields = ('product_type', 'var_name')
    list_display = ['product_type', 'var_name']

    class Meta:
        model = ProductVariations
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductVariations)
# admin.site.register(ProductImage)
