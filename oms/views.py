from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models
from oms.models import Order

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

#Employee views
class EmployeeListView(ListView):
    #Default ListView takes the model name, lowercase it and creates the context listself.
    #In this case it would be products_list -> this could be modified by using context_object_name
    context_object_name = 'employees'
    model = models.Employee

class EmployeeDetailView(DetailView):
    #DetailView returns the model name lowercased as context i.e. 'product'
    context_object_name = 'employee_detail'
    model = models.Employee
    template_name = 'oms/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = models.Employee
    fields = ['fname','lname', 'country', 'address', 'telephone']

class EmployeeUpdateView(UpdateView):
    model = models.Employee
    fields =  ['fname','lname', 'country', 'address', 'telephone']

class EmployeeDeleteView(DeleteView):
    model = models.Employee
    success_url = reverse_lazy('oms:employee_list')

#Orders views
class OrderListView(ListView):
    #Default ListView takes the model name, lowercase it and creates the context listself.
    #In this case it would be products_list -> this could be modified by using context_object_name
    context_object_name = 'orders'
    model = models.Order
    queryset = Order.objects.order_by('id')

class AssignedOrderListView(ListView):
    #Default ListView takes the model name, lowercase it and creates the context listself.
    #In this case it would be products_list -> this could be modified by using context_object_name
    context_object_name = 'orders'
    model = models.Order
    queryset = Order.objects.order_by('id')
    queryset = Order.objects.filter(status='ASSIGNED')
    template_name = 'oms/assigned_order_list.html'

class NewOrderListView(ListView):
    #Default ListView takes the model name, lowercase it and creates the context listself.
    #In this case it would be products_list -> this could be modified by using context_object_name
    context_object_name = 'orders'
    model = models.Order
    queryset = Order.objects.order_by('id')
    queryset = Order.objects.filter(status='NEW')
    template_name = 'oms/new_order_list.html'

class FinishedOrderListView(ListView):
    #Default ListView takes the model name, lowercase it and creates the context listself.
    #In this case it would be products_list -> this could be modified by using context_object_name
    context_object_name = 'orders'
    model = models.Order
    queryset = Order.objects.order_by('id')
    queryset = Order.objects.filter(status='FINISHED')
    template_name = 'oms/finished_order_list.html'

class OrderDetailView(DetailView):
    #DetailView returns the model name lowercased as context i.e. 'product'
    context_object_name = 'order_detail'
    model = models.Order
    template_name = 'oms/order_detail.html'

class OrderCreateView(CreateView):
    model = models.Order
    fields = ['assigned','status', 'product', 'table', 'timestamp','due_date']

class OrderUpdateView(UpdateView):
    model = models.Order
    fields = ['assigned','status', 'product', 'table', 'timestamp','due_date']

class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy('oms:order_list')
