"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# backend/urls.py
from shop import views

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.generic import RedirectView


def home(request):
    return JsonResponse({
        "message": "Welcome to the E-Commerce API 👋",
        "available_endpoints": {
            "Admin Panel": "/admin/",
            "Token Obtain": "/api/token/",
            "Token Refresh": "/api/token/refresh/",
            "Products API": "/api/products/",
            "Orders API": "/api/orders/"
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    # include app urlconfs (these should define /api/token/ etc.)
    path('api/accounts/', include('accounts.urls')), 
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('api.urls')), 
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('', home),
    path('', include('shop.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
