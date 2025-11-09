from rest_framework import serializers
# from .models import Product, OrderItem, Order
from .models import Product
from orders.models import Order, OrderItem

# First: Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Then: Order item serializer (which uses ProductSerializer)
class OrderItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_detail', 'qty', 'price')

# Finally: Order serializer (if you have it)
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
