from django.urls import path
from oms import views

app_name = 'oms'

urlpatterns = [
    #index view
    path('',views.IndexView.as_view(),name='index'),
    #product views
    path('productlist/',views.ProductListView.as_view(),name='product_list'),
    path('productlist/<int:pk>/',views.ProductDetailView.as_view(), name = 'product_detail'),
    path('productcreate/',views.ProductCreateView.as_view(), name = 'product_create'),
    path('productupdate/<int:pk>/',views.ProductUpdateView.as_view(), name = 'product_update'),
    path('productdelete/<int:pk>/',views.ProductDeleteView.as_view(), name = 'product_delete'),
    #employee views
    path('register/',views.register,name='register'),
]
