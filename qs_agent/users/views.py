from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datacenter.models import Orders


def home(request):
    return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PlacedOrdersByUserListView(LoginRequiredMixin, generic.ListView):
    """
        Generic class-based view listing orders to current user.
    """
    model = Orders
    template_name = 'templates/orders.html'

    def get_orders(self):
        Orders.objects.filter(user=self.request.user)