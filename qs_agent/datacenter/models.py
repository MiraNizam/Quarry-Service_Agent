from django.db import models


class Orders(models.Model):
    is_delivered = models.BooleanField(default=False)
    part_no = models.CharField(max_length=50)
    eng_description = models.CharField(max_length=100)
    rus_description = models.CharField(max_length=100)
    q_ty = models.IntegerField(default=1)
    lead_time = models.CharField(max_length=50)
    etd_eta = models.CharField(max_length=50)
    delivery_date = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)




