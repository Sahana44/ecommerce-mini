from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('', views.product_list, name='product_list'),
]
