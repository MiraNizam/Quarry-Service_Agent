from django.contrib import admin
from datacenter.models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'manager')
    list_filter = ('order_id', 'manager')
