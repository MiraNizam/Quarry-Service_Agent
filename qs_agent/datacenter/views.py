from .models import Orders
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from tablib import Dataset
from .resources import OrdersResource


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


def import_excel(request):
    if request.method == 'POST':
        orders = OrdersResource()
        dataset = Dataset()
        new_orders = request.FILES['my_file']
        imported_data = dataset.load(new_orders.read())
        result = orders.import_data(dataset, dry_run=True)
        if not result.has_errors():
            orders.import_data(dataset, dry_run=False)
    return render(request, 'import.html', {})




