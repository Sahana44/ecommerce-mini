# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse


def product_list(request):
    return JsonResponse({
        "products": [
            {"id": 1, "name": "Product A", "price": 100},
            {"id": 2, "name": "Product B", "price": 150}
        ]
    })

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')

    # queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'slug', 'category']
