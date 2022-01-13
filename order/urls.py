from django.urls import path
from .views import DriverList, ClientList, OrderList, OrderUpdate, OrderListByClient


urlpatterns = [
    path('create-driver/', DriverList.as_view(), name='create-driver'),
    path('create-client/', ClientList.as_view(), name='create-client'),
    path('create/', OrderList.as_view(), name='create-order'),
    path('update-status/<int:pk>/', OrderUpdate.as_view(), name='update-order-status'),
    path('orders/clients/<int:pk>/', OrderListByClient.as_view(), name='list-client-order')
]