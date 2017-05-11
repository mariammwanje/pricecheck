from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from sellers.models import Seller
from .models import SellerProduct


class CreateSellerView(CreateView):
    model = Seller
    fields = ['name', 'contact', 'address', 'email', 'country', 'contact_person','seller_logo']
    success_url = reverse_lazy('sellers:seller_list')
    template_name = 'sellers/add_seller.html'


class ListSellerView(ListView):
    model = Seller
    template_name = 'sellers/seller_list.html'

    queryset = Seller.objects.all()

    def get_queryset(self, *args, **kwargs):
        seller_data = super(ListSellerView, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('search')
        if q:
            seller_data = self.model.objects.filter(Q(name__icontains=q))
            print(seller_data)
            return seller_data
        print(seller_data)
        return seller_data

    def get_context_data(self, **kwargs):
        context = super(ListSellerView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DeleteSellerView(DeleteView):
    model = Seller
    success_url = reverse_lazy('sellers:seller_list')
    template_name = 'sellers/delete_seller.html'


class UpdateSellerView(UpdateView):
    model = Seller
    fields = ['name', 'contact', 'address', 'email', 'country', 'contact_person','seller_logo']
    success_url = reverse_lazy('sellers:seller_list')
    template_name = 'sellers/edit_seller.html'


class DetailSellerView(DetailView):
    model = Seller
    success_url = reverse_lazy('sellers:seller_list')
    template_name = 'sellers/detail_seller.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        seller_product = self.get_object()

        seller_product_list = SellerProduct.objects.filter(product_name=seller_product.id)
        context['seller_product_list'] = seller_product_list



        return context


        ###########################
        # sellerproduct
        #########################


class CreateSellerProductView(CreateView):
    model = SellerProduct
    fields = ['seller_name', 'product_name', 'seller_price','quantity', 'category', 'seller_product_image']
    template_name = 'sellers/seller_product_add.html'
    success_url = reverse_lazy('sellers:seller_product_list')


class ListSellerProductView(ListView):
    model = SellerProduct
    template_name = 'sellers/seller_product_list.html'
    queryset = Seller.objects.all()

    def get_queryset(self, *args, **kwargs):
        sellerproduct_data = super(ListSellerProductView, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('search')
        if q:
            sellerproduct_data = self.model.obje2cts.filter(Q(sellerproduct_name__icontains=q))
            print(sellerproduct_data)
            return sellerproduct_data
        print(sellerproduct_data)
        return sellerproduct_data

    def get_context_data(self, **kwargs):
        context = super(ListSellerProductView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

        #
        # class DeleteSellerProductView(DeleteView):
        #     model = SellerProduct
        #     success_url = reverse_lazy('sellers:seller_product_list')
        #     template_name = 'sellers/seller_product_delete.html'
        #
        #
        # class UpdateSellerProductView(UpdateView):
        #     model = SellerProduct
        #     fields = ['seller_name', 'product_name', 'seller_price']
        #     success_url = reverse_lazy('sellers:seller_product_list')
        #     template_name = 'sellers/seller_product_edit.html'
        #
        #
        # class DetailSellerProductView(DetailView):
        #     model = Seller
        #     success_url = reverse_lazy('sellers:seller_product_list')
        #     #template_name = 'sellers/seller_detail.html'
