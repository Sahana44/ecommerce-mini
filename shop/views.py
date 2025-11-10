

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from products.models import Product
from orders.models import Order
User = get_user_model()


def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # ✅ Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return redirect("register")

        # Create new user
        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")

    return render(request, "register.html")

def admin_dashboard(request):
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    recent_orders = Order.objects.all().order_by('-created_at')[:5]

    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'recent_orders': recent_orders,
    }
    return render(request, 'shop/admin_dashboard.html', context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'message': 'User registered successfully!'})
    
    # For GET request → render HTML form
    return render(request, 'register.html')
from django.shortcuts import render
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the E-Commerce API"})

def login_view(request):
    return JsonResponse({"message": "Login API endpoint - use /api/accounts/login/"})

def register_view(request):
    return JsonResponse({"message": "Register API endpoint - use /api/accounts/register/"})

def admin_dashboard(request):
    return JsonResponse({"message": "Admin Dashboard placeholder"})
from django.shortcuts import render

def home_view(request):
    return render(request, 'shop/home.html')

def login_view(request):
    return render(request, 'shop/login.html')

def register_view(request):
    return render(request, 'shop/register.html')

def admin_dashboard(request):
    return render(request, 'shop/admin_dashboard.html')
