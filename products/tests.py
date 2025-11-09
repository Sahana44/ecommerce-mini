from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from products.models import Product

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_products_list(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class AdminAPITestCase(TestCase):
    def setUp(self):
        # Create admin user
        self.admin = User.objects.create_superuser(username="admin", password="admin123", email="admin@example.com")
        self.client = APIClient()

    def authenticate_admin(self):
        self.client.login(username="admin", password="admin123")
        def test_admin_login_valid_and_invalid(self):
            response = self.client.post("/api/token/", {"username": "admin", "password": "admin123"}, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Invalid login
            response = self.client.post("/api/token/", {"username": "admin", "password": "wrongpass"}, format="json")
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        def test_get_products_returns_paginated_list(self):
            self.authenticate_admin()
            response = self.client.get("/api/products/")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn("results", response.data)
        def test_add_product_missing_fields(self):
            self.authenticate_admin()
            payload = {"name": "", "price": ""}
            response = self.client.post("/api/products/", payload, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        def test_update_product(self):
            self.authenticate_admin()
            product = Product.objects.create(name="Test Product", price=100, description="Demo", category="Books")
            response = self.client.put(f"/api/products/{product.id}/", {
                "name": "Updated Product", "price": 150, "description": "Updated", "category": "Books"
                }, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["name"], "Updated Product")
        def test_delete_product(self):
            self.authenticate_admin()
            product = Product.objects.create(name="Delete Me", price=50, description="Demo", category="Toys")
            response = self.client.delete(f"/api/products/{product.id}/")
            self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_200_OK])
        def test_unauthorized_user_access_admin_endpoints(self):
            response = self.client.get("/api/products/")
            self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
from rest_framework.test import APITestCase
from rest_framework import status
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class AdminProductTests(APITestCase):
    def setUp(self):
        # Create admin user
        self.admin_user = User.objects.create_superuser(username="admin", password="admin123")
        # Login and get token
        response = self.client.post("/api/token/", {"username": "admin", "password": "admin123"}, format="json")
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_get_all_products(self):
        """TC-A2: GET /api/products/ should return paginated list"""
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertIn("count", response.data)
        print("✅ TC-A2 passed: Products list retrieved successfully")

    def test_create_product_with_missing_fields(self):
        # """TC-A3: POST /api/products with missing fields should return 400"""
        incomplete_data = {
            "name": "",  # Missing required fields like price, description, etc.
        }
        response = self.client.post("/api/products/", incomplete_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("✅ TC-A3 passed: Missing fields returned 400 Bad Request")
    def test_update_product(self):
    # """TC-A4: PUT /api/admin/products/:id updates product fields correctly"""
    # First, create a product
        product = Product.objects.create(
            name="Old Laptop",
            description="Old description",
            price=80000,
            stock=5,
        )

    # Prepare updated data
        updated_data = {
            "name": "Updated Laptop",
            "description": "Updated description",
            "price": 85000,
            "stock": 10,
        }

    # Authenticate as admin (created in setUp)
        self.client.force_authenticate(user=self.admin_user)

    # Make PUT request
        response = self.client.put(f"/api/products/{product.id}/", updated_data, format="json")

    # Verify response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Updated Laptop")
        self.assertEqual(response.data["price"], 85000)

    def test_delete_product(self):
    # """TC-A5: DELETE /api/admin/products/:id removes product"""
    # Create a product to delete
        product = Product.objects.create(
            name="Test Product",
            description="To be deleted",
            price=1000,
            stock=2,
        )

    # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)

    # Perform DELETE request
        response = self.client.delete(f"/api/products/{product.id}/")

    # Check that it returns 204 (No Content)
        self.assertEqual(response.status_code, 204)

    # Verify that the product no longer exists
        exists = Product.objects.filter(id=product.id).exists()
        self.assertFalse(exists)

