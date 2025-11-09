from django.urls import path
from . import views
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API 👋",
        "endpoints": {
            "Products": "/api/products/",
            "Orders": "/api/orders/"
        }
    })

urlpatterns = [
    path('', api_root),
]
