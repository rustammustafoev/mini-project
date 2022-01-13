from django.contrib import admin
from django.contrib.admin import register
from . import models


@register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'car_type']


@register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone_number']


@register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_status', 'order_start_time']

