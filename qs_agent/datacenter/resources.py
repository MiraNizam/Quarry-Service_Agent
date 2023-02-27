from import_export import resources
from .models import Orders


class OrdersResource(resources.ModelResource):
    class Meta:
        model = Orders
        