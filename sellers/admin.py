from django.contrib import admin

from .models import Seller, SellerProduct


class SellerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'contact', 'address', 'email', 'country',
                     'contact_person')

    list_display = ['name', 'contact','country', 'contact_person']

    class Meta:
        model = Seller


class SellerProductAdmin(admin.ModelAdmin):
    search_fields = ("product_name", "seller_name")
    list_display = ['product_name__name', 'seller_name__field1']

    class Meta:
        model = SellerProduct


admin.site.register(Seller)
admin.site.register(SellerProduct)
