from audioop import reverse

from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="media/category")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='media/products')

    def __str__(self):
        return self.product_name

    def get_price(self):
        return str(self.price)

    def get_absolute_url(self):
        return reverse("products_landing")

    def get_image_url(self):
        img = self.productimage_set.first()
        if img:
            return img.image.url
        return img


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.product_id)


class ProductVariations(models.Model):
    product_type = models.ForeignKey(Product)
    var_name = models.CharField(max_length=100)
    var_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    sales_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)

    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.product_type)

    # checking to return var price if sales price is not None
    def get_price(self):
        if self.sales_price is not None:
            return self.sales_price
        else:
            return self.var_price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

# function that handles wat we are working on
# def product_saved_reciever(sender, instance, created,
#                            *args, **kwargs):
#     product = instance
#     productvariations = product.productvariations_set.all()
#     if productvariations.count == 0:
#         new_var = ProductVariations()
#         new_var.product = product
#         new_var.product_type = 'Default'
#         new_var.var_price = product.price
#         new_var.save()
#
# post_save.connect(product_saved_reciever,sender=Product)
