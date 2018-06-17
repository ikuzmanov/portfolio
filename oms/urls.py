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
    path('employeelist/',views.EmployeeListView.as_view(),name='employee_list'),
    path('employeelist/<int:pk>/',views.EmployeeDetailView.as_view(), name = 'employee_detail'),
    path('employeecreate/',views.EmployeeCreateView.as_view(), name = 'employee_create'),
    path('employeeupdate/<int:pk>/',views.EmployeeUpdateView.as_view(), name = 'employee_update'),
    path('employeetdelete/<int:pk>/',views.EmployeeDeleteView.as_view(), name = 'employee_delete'),
    #order views
    path('orderlist/',views.OrderListView.as_view(),name='order_list'),
    path('assignedorderlist/',views.AssignedOrderListView.as_view(),name='assigned_order_list'),
    path('neworderlist/',views.NewOrderListView.as_view(),name='new_order_list'),
    path('finishedorderlist/',views.FinishedOrderListView.as_view(),name='finished_order_list'),
    path('orderlist/<int:pk>/',views.OrderDetailView.as_view(), name = 'order_detail'),
    path('ordercreate/',views.OrderCreateView.as_view(), name = 'order_create'),
    path('orderupdate/<int:pk>/',views.OrderUpdateView.as_view(), name = 'order_update'),
    path('ordertdelete/<int:pk>/',views.OrderDeleteView.as_view(), name = 'order_delete'),
]
