from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Order
from products.models import Product
# Create your tests here.
class AdminOrderTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()

        # Create admin user
        self.admin_user = self.User.objects.create_superuser(
            username="admin", password="admin123"
        )

        # Create sample product
        self.product = Product.objects.create(
            name="Laptop",
            description="Gaming laptop",
            price=1500.00,
            stock=10,
        )

        # Create some sample orders
        self.order_pending = Order.objects.create(
            user=self.admin_user,
            total=1500.00,
            shipping_address="Bengaluru",
            status="Pending",
        )
        self.order_completed = Order.objects.create(
            user=self.admin_user,
            total=2000.00,
            shipping_address="Mysuru",
            status="Completed",
        )
    def test_filter_orders_by_status(self):
    # """TC-A6: GET /api/orders?status=Pending filters results"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get("/api/orders/?status=Pending")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(all(o["status"] == "Pending" for o in data["results"]))
    def test_update_order_status(self):
    # """TC-A7: PUT /api/orders/:id/status updates status and persists"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(
            f"/api/orders/{self.order_pending.id}/",
            {"status": "Shipped"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

    # Check if status changed in DB
        self.order_pending.refresh_from_db()
        self.assertEqual(self.order_pending.status, "Shipped")

    def test_unauthorized_access(self):
    # """TC-A8: Unauthorized user calling admin endpoints receives 401/403"""
    # Try to access admin API without authentication
        response = self.client.get("/api/orders/")
        self.assertIn(response.status_code, [401, 403])

    # Create a normal (non-admin) user
        normal_user = self.User.objects.create_user(
            username="normal", password="user123"
    )

    # Authenticate as a normal user
        self.client.force_authenticate(user=normal_user)
        response = self.client.get("/api/orders/")
        self.assertIn(response.status_code, [401, 403])
