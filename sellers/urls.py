from django.conf.urls import url

from . import views

urlpatterns = [url(r'sellers/add/$', views.CreateSellerView.as_view(), name='add_seller'),
    url(r'^$', views.ListSellerView.as_view(), name='seller_list'),
    url(r'sellers/(?P<pk>\d+)/delete/$', views.DeleteSellerView.as_view(), name='delete_seller'),
    url(r"sellers/(?P<pk>\d+)/edit/$", views.UpdateSellerView.as_view(), name='edit_seller'),
    url(r"sellers/(?P<pk>\d+)details/$", views.DetailSellerView.as_view(), name='detail_seller'),

    url(r'sellersproducts/add/$', views.CreateSellerProductView.as_view(), name='seller_product_add'),
    url(r'^$', views.ListSellerProductView.as_view(), name='seller_product_list'),
    # url(r'sellersproducts/(?P<pk>\d+)/delete/$', views.DeleteSellerProductView.as_view(), name='seller_product_delete'),
    # url(r"sellersproducts/(?P<pk>\d+)/edit/$", views.UpdateSellerProductView.as_view(), name='seller_product_edit'),
    # url(r"sellersproducts/(?P<pk>\d+)details/$", views.DetailSellerProductView.as_view(), name='seller_product_detail'),
    #
]