# # from rest_framework import serializers
# # from .models import Product

# # class ProductSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Product
# #         fields = '__all__'
# # # users/serializers.py
# # from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# # from rest_framework import serializers
# # from .models import User

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Optionally put custom claims in the token itself:
#         token['role'] = getattr(user, 'role', '')
#         token['email'] = user.email
#         return token

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         # Attach extra fields to the response (not only inside token)
#         data['username'] = self.user.username
#         data['email'] = self.user.email
#         data['role'] = getattr(self.user, 'role', '')
#         return data


# from rest_framework import serializers
# # from .models import Order, OrderItem
# from .models import Product

# # from products.serializers import ProductSerializer

# class OrderItemSerializer(serializers.ModelSerializer):
#     product_detail = ProductSerializer(source='product', read_only=True)
#     class Meta:
#         model = OrderItem
#         fields = ('id','product','product_detail','qty','price')

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True)
#     class Meta:
#         model = Order
#         fields = ('id','user','items','total','shipping_address','status','admin_notes','created_at')
#         read_only_fields = ('created_at','status')

#     def create(self, validated_data):
#         items_data = validated_data.pop('items', [])
#         user = self.context['request'].user if self.context['request'].user.is_authenticated else None
#         order = Order.objects.create(user=user, **validated_data)
#         total = 0
#         for it in items_data:
#             prod = it.get('product')
#             qty = it.get('qty',1)
#             price = it.get('price') or (prod.price if prod else 0)
#             OrderItem.objects.create(order=order, product=prod, qty=qty, price=price)
#             total += float(price) * int(qty)
#         order.total = total
#         order.save()
#         return order

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'






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
