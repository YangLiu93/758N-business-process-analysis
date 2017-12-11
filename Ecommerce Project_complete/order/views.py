from django.views import generic
from .models import Orders, Product, ProductOrder, return_order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import return_orderForm


class IndexView(generic.ListView):
    template_name = 'order/index.html'
    context_object_name = 'all_Return'
    def get_queryset(self):
        return return_order.objects.all()

class DetailView(LoginRequiredMixin,generic.DeleteView):
    model = return_order
    template_name = 'order/detail.html'

class ReturnCreate(LoginRequiredMixin,CreateView):
    form_class = return_orderForm
    template_name = 'order/return_order_form.html'
    #model = return_order
    #fields = ['ProductId', 'ReturnReason', 'ReturnOptions', 'ProductQuality']

    def get_form_kwargs(self):
        kwargs = super(ReturnCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class ReturnUpdate(LoginRequiredMixin,UpdateView):
    model = return_order
    fields = ['ProductId', 'ReturnReason', 'ReturnOptions', 'ProductQuality']

class ReturnDelete(LoginRequiredMixin,DeleteView):
    model = return_order
    success_url = reverse_lazy('order:return_items')

# Create your views here.

'''
@login_required
def return_status(request):
    all_Return = return_order.objects.select_related('ProductId')
    all_obj = return_order.objects.select_related('ProductId')
    context = {'all_Return': all_Return,
               'all_obj': all_obj,
               }
    return render(request,'order/return_items_list.html',context)

'''
'''
@login_required
def all_products(request):
    all_products_list = Product.objects.all()
    context = {'all_products_list': all_products_list}
    return render(request, 'order/products_list.html',context)
'''


@login_required
def each_product(request, proid):
    specific_product = Product.objects.get(pk=proid)
    context = {'specific_product': specific_product}
    return render(request, 'order/each_product.html',context)

class all_ProductsView(LoginRequiredMixin,generic.ListView):
    template_name = 'order/products_list.html'
    context_object_name = 'all_products_list'
    def get_queryset(self):
        return Product.objects.filter(ProBuyer=self.request.user)

class return_statusView(LoginRequiredMixin,generic.ListView):
    template_name = 'order/return_items_list.html'
    context_object_name = 'all_Return'
    def get_queryset(self):
        return return_order.objects.select_related('ProductId').filter(ProductId__ProBuyer=self.request.user)

