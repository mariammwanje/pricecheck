# Create your views here.

from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from products.models import Product, Category, ProductVariations, ProductImage


class CreateProductView(CreateView):
    model = Product
    fields = ['product_name', 'price', 'categories', 'description', 'category', 'image', 'default', 'active']

    success_url = reverse_lazy("products:products_landing")
    template_name = 'products/create_products'


class ProductListView(ListView):
    model = Product
    template_name = 'products/products_landing.html'
    # picking all the products created objects
    queryset = Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        product_data = super(ProductListView, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('search')
        if q:
            product_data = self.model.objects.filter(Q(product_name__icontains=q))
            print(product_data)
            return product_data
        print(product_data)
        return product_data

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy("products:products_landing")
    template_name = 'products/products_details.html'


class CreateProductImage(CreateView):
    model = ProductImage
    fields = ['product_id', 'img']


class ProductImageList(ListView):
    model = ProductImage


class CreateCategoryView(CreateView):
    model = Category
    fields = ['category_name', 'image', 'description', 'active', 'timestamp']

    success_url = reverse_lazy("products:category_landing")
    template_name = 'products/create_category.html'

class CategoryDetailView(DetailView):
    model = Category
    success_url = reverse_lazy("products:category_landing")
    template_name = 'products/category_details.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_landing.html'
    queryset = Category.objects.all()

    def get_queryset(self, *args, **kwargs):
        category_data = super(CategoryListView, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('search_category')
        if q:
            category_data = self.model.objects.filter(
                Q(category_name__icontains=q)
            )
            return category_data
        return category_data

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateProductVariations(CreateView):
    model = ProductVariations
    fields = ['product_type', 'var_name', 'var_price', ' sales_price', 'active']
    success_url = reverse_lazy("products:create_variations")
    template_name = 'products/product_variations_landing.html'


class ProductVariationsListView(ListView):
    model = ProductVariations
    template_name = 'products/product_variations_landing.html'
