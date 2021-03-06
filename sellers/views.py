from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from sellers.models import Seller, SellerProduct


class CreateSellerView(CreateView):
    model = Seller
    fields = ['name', 'contact', 'address', 'email', 'country', 'contact_person', 'seller_logo']
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
    fields = ['name', 'contact', 'address', 'email', 'country', 'contact_person', 'seller_logo']
    success_url = reverse_lazy('sellers:seller_list')
    template_name = 'sellers/edit_seller.html'


class DetailSellerView(DetailView):
    model = Seller
    success_url = reverse_lazy('sellers:seller_list')
    template_name = 'sellers/detail_seller.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        seller = self.get_object()

        seller_list = Seller.objects.filter(name=seller.id)
        context['seller_list'] = seller_list

        return context


        ###########################
        # sellerproduct
        #########################


#
#
class CreateSellerProductView(CreateView):
    model = SellerProduct
    fields = ['seller_name', 'name_product', 'seller_price', 'image'
              ]
    template_name = 'sellers/sellerproduct_add.html'
    success_url = reverse_lazy('sellers:sellerproduct_list')


class ListSellerProductView(ListView):
    model = SellerProduct
    template_name = 'sellers/sellerproduct_list.html'
    queryset = SellerProduct.objects.all()

    def get_queryset(self, *args, **kwargs):
        sellerproduct_data = super(ListSellerProductView, self).get_queryset(*args, **kwargs)
        q = self.request.GET.get('search_sellerproduct')
        if q:
            sellerproduct_data = self.model.objects.filter(
                Q(name_product__product_name__icontains=q)|
                Q(seller_name__name__icontains=q))
            return sellerproduct_data
        return sellerproduct_data

    def get_context_data(self, **kwargs):
        context = super(ListSellerProductView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
