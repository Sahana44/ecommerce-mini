# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import OrderViewSet

# router = DefaultRouter()
# router.register(r'orders', OrderViewSet, basename='order')

# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from . import views

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('', views.order_list, name='order_list'),

]
