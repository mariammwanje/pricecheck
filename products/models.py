from audioop import reverse

from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="media/category")

    def __str__(self):
        return self.category_name


class CreateCategory(models.Model):
    model = Category
    fields = ['category_name', 'image', 'description']


class CategoryListView(models.Model):
    model = Category


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.CharField(max_length=100)
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


class CreateProduct(models.Model):
    model = Product
    fields = ['product_name', 'price', 'quantity', ' category', 'image']


class ProductListView(models.Model):
    model = Product


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.product_id)


class CreateProductImage(models.Model):
    model = ProductImage
    fields = ['product_id', 'img']


class ProductImageList(models.Model):
    model = ProductImage


class ProductVariations(models.Model):
    product_type = models.ForeignKey(Product)
    variation_name = models.CharField(max_length=100)
    sale_prices = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.product_type)


class CreateProductVariations(models.Model):
    model = ProductVariations
    fields = ['product_type', 'variation_name', ' sale_prices', ' price']


class ProductVariationsListView(models.Model):
    model = ProductVariations
