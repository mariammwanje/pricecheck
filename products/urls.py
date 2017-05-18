# import user

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"(?P<pk>\d+)details/$", views.ProductDetailView.as_view(), name='products_details'),

    url(r'^$', views.ProductListView.as_view(), name='products_landing'),
    url(r"create$", views.CreateProductView.as_view(), name='create_products'),
    url(r"create$", views.CreateCategoryView.as_view(), name='create_category'),
    url(r"list$", views.CategoryListView.as_view(), name='category_landing'),

    #product variations
    url(r'variations/$', views.ProductVariationsListView.as_view(), name='product_variations_landing'),
    url(r"create_variations/$", views.CreateProductVariations.as_view(), name='create_variations'),

]
