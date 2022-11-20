from .models import Orders
from django.shortcuts import render


def orders_qs(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders.html', context)


def user_profile(request):
    return render(request, "profile.html")

