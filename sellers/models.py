from django.db import models
from django.urls import reverse

from products.models import Product


# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    seller_logo = models.ImageField(upload_to='media/sellers', default=1)

    def __str__(self):
        return self.name


class CreateSeller(models.Model):
    model = Seller
    fields = ['name', 'contact', 'address', 'email', 'country', 'contact_person', 'seller_logo']


class UpdateSeller(models.Model):
    model = Seller
    fields = ['name', 'contact', 'address', 'email', 'country', 'contact_person', 'seller_logo']


class SellerList(models.Model):
    model = Seller


class SellerProduct(models.Model):
    product_name = models.ForeignKey(Product)
    seller_name = models.ForeignKey(Seller)
    seller_price = models.IntegerField()
    # seller_product_image = models.ImageField(upload_to='media/sellers', default=1)
    image = models.ImageField(upload_to='media/sellers')

    def __str__(self):
        return str(self.product_name)

    def get_price(self):
        return str(self.seller_name)

    def get_price(self):
        return str(self.seller_price)

    def get_absolute_url(self):
        return reverse("sellerproduct_list")

    def get_image_url(self):
        img = self.sellerproduct_image_set.first()
        if img:
            return img.image.url
        return img
#
#
class CreateSellerProduct(models.Model):
    model = SellerProduct
    fields = ['product_name', 'seller_name', 'seller_price', 'image']
#
#
class SellerProductListView(models.Model):
    model = SellerProduct
