# # from django.shortcuts import render

# # Create your views here.
# # from rest_framework_simplejwt.views import TokenObtainPairView
# # class MyTokenObtainPairView(TokenObtainPairView):
# #     serializer_class = MyTokenObtainPairSerializer
# # users/views.py (add imports)
# # from rest_framework_simplejwt.views import TokenObtainPairView
# # from .serializers import MyTokenObtainPairSerializer

# # # Custom view that tells SimpleJWT to use our serializer
# # class MyTokenObtainPairView(TokenObtainPairView):
# #     serializer_class = MyTokenObtainPairSerializer



# from rest_framework import viewsets
# from django.contrib.auth import get_user_model

# from .serializers import MyTokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.permissions import IsAdminUser
# from rest_framework.serializers import ModelSerializer

# # Token View
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# # Simple User Serializer for Admin
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_staff']

# # Admin ViewSet for managing users
# class UserAdminViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

User = get_user_model()  # ✅ Use your custom user model

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
