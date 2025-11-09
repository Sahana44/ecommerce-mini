from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.http import JsonResponse

def order_list(request):
    return JsonResponse({
        "orders": [
            {"id": 1, "product": "Product A", "quantity": 2},
            {"id": 2, "product": "Product B", "quantity": 1}
        ]
    })

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
