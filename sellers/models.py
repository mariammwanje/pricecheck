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

    # seller_logo = models.ImageField(upload_to='media/products', default=1)

    def __str__(self):
        return self.name


class SellerProduct(models.Model):
    name_product = models.ForeignKey(Product)
    seller_name = models.ForeignKey(Seller)
    seller_price = models.IntegerField()
    # seller_product_image = models.ImageField(upload_to='media/sellers', default=1)
    image = models.ImageField(upload_to='media/products')

    def __str__(self):
        return str(self.name_product)

    def get_price(self):
        return str(self.seller_price)

    def get_absolute_url(self):
        return reverse("sellerproduct_list")

    def get_image_url(self):
        img = self.sellerproduct_image_set.first()
        if img:
            return img.image.url
        return img


class SellerProductVariation(models.Model):
    pass
