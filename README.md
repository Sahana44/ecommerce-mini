🧑‍💼 Admin Demo Steps 
🔹 1. Start the Server

Run the Django development server:

python manage.py runserver

The backend will start at:
👉 http://127.0.0.1:8000/

🔹 2. Access the Admin Panel

Open this URL in your browser:

http://127.0.0.1:8000/admin/

🔹 3. Admin Credentials

Use the following credentials to log in:

Username: admin@example.com
Password: Admin@12345


💡 If you want to create a new admin account, run:

python manage.py createsuperuser

🔹 4. Admin Dashboard Overview

|        Action               |                      Description                                            |
| --------------------------  | --------------------------------------------------------------------------- |
| 🛍️ **Add Product**          | Click **“Add Product”** under the Products section to create a new product. |
| ✏️ **Edit Product**         | Click a product name to update its details.                                 |
| ❌ **Delete Product**       | Remove or deactivate products no longer available.                          |
| 📦 **View Orders**          | Review all user orders in the Orders section.                               |
| 🔄 **Update Order Status**  | Change status from Pending → Processing → Shipped → Delivered.              |
| 📤 **Export Orders (CSV)**  | Export selected orders to a CSV file for reporting.                         |



🔹 5. Test Admin APIs (Optional)

You can test the backend APIs using Postman or cURL.

Obtain JWT Token:

curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d "{\"username\": \"admin@example.com\", \"password\": \"Admin@12345\"}"


Response example:

{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}


Use the token to access protected endpoints:

curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/orders/

🔹 6. Admin Features Demonstration
        Feature           	       Description
✅ Login Authentication  : 	Secure JWT-based login
📦 Product CRUD	         :   Create, Read, Update, Delete products
🧾 Order Management	     :   Track and update orders
📊 Dashboard Metrics	 :    See total sales and active orders
📤 CSV Export	         :     Download reports easily


🔹 7. Logout / End Session

Log out using the admin dashboard (top-right corner), or

Remove the JWT token if testing via API tools.