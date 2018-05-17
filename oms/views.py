from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models
from oms.forms import UserForm

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

# 2) Employee registrations / login views

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'oms/employee_registration.html',
                    {'user_form':user_form,
                    'registered':registered})
