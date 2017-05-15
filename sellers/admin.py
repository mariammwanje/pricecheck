from django.contrib import admin

# Register your models here.

from .models import Seller, SellerProduct


class SellerAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'seller_name']
    list_display = ['product_name', 'seller_name']

    class Meta:
        model = Seller

admin.site.register(Seller)
admin.site.register(SellerProduct)

