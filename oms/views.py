from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models

# 1) Product page views
class IndexView(TemplateView):
    template_name = 'oms/oms_base.html'

class ProductListView(ListView):
    #Default ListView takes the model name, lowercase it and creates the context listself.
    #In this case it would be products_list -> this could be modified by using context_object_name
    context_object_name = 'products'
    model = models.Product

class ProductDetailView(DetailView):
    #DetailView returns the model name lowercased as context i.e. 'product'
    context_object_name = 'product_detail'
    model = models.Product
    template_name = 'oms/product_detail.html'

class ProductCreateView(CreateView):
    model = models.Product
    fields = ['name','price', 'quantity', 'description', 'active']

class ProductUpdateView(UpdateView):
    model = models.Product
    fields = ['name','price', 'quantity', 'description', 'active']

class ProductDeleteView(DeleteView):
    model = models.Product
    success_url = reverse_lazy('oms:product_list')
