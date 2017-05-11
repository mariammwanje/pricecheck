# import user

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.ProductListView.as_view(), name='products_landing'),
    url(r"products/create$", views.CreateProductView.as_view(), name='create_products'),


]
