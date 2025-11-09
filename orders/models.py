# from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [('Pending','Pending'), ('Processing','Processing'), ('Shipped','Shipped'), ('Delivered','Delivered'), ('Cancelled','Cancelled')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.JSONField()  # keep simple: store address as JSON
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
