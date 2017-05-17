from django.shortcuts import render
# from django.views.generic import TemplateView

# from products.models import Product

from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
# class HomeView(TemplateView):
#     # login_url = 'users:login'
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data()
#         context['products'] = Product.objects.all()
#         return context

def home(request):
    return render(request, 'home.html')
# class Layout(LoginRequiredMixin, TemplateView):
#     template_name = 'layout.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Layout, self).get_context_data()
#         context['products'] = Category.objects.all()
#         return context
