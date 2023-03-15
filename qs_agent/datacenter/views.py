from django.utils.datastructures import MultiValueDictKeyError

from .models import Orders
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
import pandas as pd
from django.core.files.storage import FileSystemStorage


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


def temp(request):
    return render(request, "temple.html")


@login_required
def user_profile(request):
    return render(request, "profile.html")


@login_required
def import_excel(request):
    orders = Orders.objects.all()
    orders.delete()
    try:
        if request.method == 'POST' and request.FILES['my_file']:
            file = request.FILES['my_file']
            reading_excel_file = pd.read_excel(file)
            db_frame = reading_excel_file
            for db_frame in db_frame.itertuples():
                obj = Orders.objects.create(
                    part_no=db_frame.part_no,
                    rus_description=db_frame.rus_description,
                    q_ty=db_frame.q_ty,
                    lead_time=db_frame.lead_time,
                    etd=db_frame.etd,
                    eta=db_frame.eta,
                    delivery_date=db_frame.delivery_date,
                    order_id=db_frame.order_id,
                    manager=db_frame.manager
                )
                obj.save()
        return render(request, 'import.html', {})
    except MultiValueDictKeyError:
        return render(request, 'import.html')
