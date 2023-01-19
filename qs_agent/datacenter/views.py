from .models import Orders
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User


@login_required
def user_orders(request):
    user = User.objects.get(username=request.user)
    manager_orders = Orders.objects.filter(user_id=user.id)
    context = {
        'manager_orders': manager_orders,
        'user': user
    }
    return render(request, 'user_orders.html', context)


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def user_profile(request):
    return render(request, "profile.html")
