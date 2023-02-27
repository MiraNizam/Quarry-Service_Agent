from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    """
    Model representing detailed information about parts in orders.
    """
    part_no = models.CharField(max_length=50, null=True, blank=True)
    rus_description = models.CharField(max_length=100, null=True, blank=True)
    q_ty = models.IntegerField(null=True, blank=True)
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
