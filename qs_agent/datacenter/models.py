from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Orders(models.Model):
    """
    Model representing detailed information about parts in orders.
    """
    is_delivered = models.BooleanField(default=False)
    part_no = models.CharField(max_length=50)
    rus_description = models.CharField(max_length=100, null=True, blank=True)
    q_ty = models.IntegerField(default=1)
    lead_time = models.CharField(max_length=50, null=True, blank=True)
    etd = models.CharField(max_length=50, null=True, blank=True)
    eta = models.CharField(max_length=50, null=True, blank=True)
    delivery_date = models.CharField(max_length=50, null=True, blank=True)
    order_id = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name="Менеджер, которому принадлежит заказ")

    def get_manager(self):
        return self.manager

    def delivered_orders(self):
        if self.is_delivered:
            return self.is_delivered

    def get_absolute_url(self):
        return reverse('manager', kwargs={'user': self.pk})
