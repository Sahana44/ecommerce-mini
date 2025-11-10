🛒 E-Commerce Mini Project
🧠 Overview

This is a Full Stack E-Commerce Web Application built using Django REST Framework.
It allows users to register, log in using JWT, browse products, add to cart, and place orders.
An Admin Panel enables product and order management with authentication and authorization.

✨ Features:

👤 User Features:

1. User registration and JWT authentication

2. Browse and view product details

3. Add to cart, checkout, and view orders

4. Shipping address management

🧑‍💼 Admin Features:

1. Secure Admin Login (JWT-based)

2. Manage Products (Create, Read, Update, Delete)

3. Manage Orders (View, Filter, Update Status)

4. Dashboard Overview: Total Orders, Revenue, Pending Orders

5. Export Orders to CSV

6. Only Admins can access /api/admin/* routes

⚙️ Tech Stack:

1. Backend: Django, Django REST Framework (DRF)

2. Database: SQLite (default)

3. Authentication: JWT (SimpleJWT)

4. Admin Panel: Django Admin + Custom API Endpoints

5. Language: Python 3.12

6. Frontend: Ready for React or Django Templates (future scope)

🧩 Installation & Setup Steps:

1️⃣ Clone the Repository
git clone https://github.com/Sahana44/ecommerce-mini.git
cd ecommerce-mini

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Database Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (Optional)
python manage.py createsuperuser

6️⃣ Run the Development Server
python manage.py runserver

🚀 API Endpoints Summary
🔐 Authentication
| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| POST   | `/api/token/`         | Obtain JWT Token  |
| POST   | `/api/token/refresh/` | Refresh JWT Token |

🛍️ Products
| Method | Endpoint              | Description                 |
| ------ | --------------------- | --------------------------- |
| GET    | `/api/products/`      | Get all products            |
| POST   | `/api/products/`      | Add product (admin only)    |
| PUT    | `/api/products/<id>/` | Update product (admin only) |
| DELETE | `/api/products/<id>/` | Delete product (admin only) |


📦 Orders
| Method | Endpoint                   | Description                       |
| ------ | -------------------------- | --------------------------------- |
| GET    | `/api/orders/`             | Get user orders                   |
| POST   | `/api/orders/`             | Create new order                  |
| PUT    | `/api/orders/<id>/status/` | Update order status (admin only)  |
| GET    | `/api/orders/export/`      | Export orders to CSV (admin only) |

🧑‍💼 Admin Demo Steps
1️⃣ Start the Server
python manage.py runserver

2️⃣ Access API Root

Open in browser:
🔗 http://127.0.0.1:8000/

You should see:

{
  "message": "Welcome to the E-Commerce API 👋",
  "available_endpoints": {
    "Admin Panel": "/admin/",
    "Token Obtain": "/api/token/",
    "Token Refresh": "/api/token/refresh/",
    "Products API": "/api/products/",
    "Orders API": "/api/orders/"
  }
}

3️⃣ Login as Admin (JWT Token)
curl.exe -X POST "http://127.0.0.1:8000/api/token/" ^
-H "Content-Type: application/json" ^
-d "{\"username\":\"admin@example.com\",\"password\":\"Admin@12345\"}"


You’ll receive an access and refresh token.

4️⃣ Access Django Admin Panel

Go to:
🔗 http://127.0.0.1:8000/admin/

Login with:

Email: admin@example.com
Password: Admin@12345

5️⃣ Manage Products

1. Navigate to Products → Add Product

2. Add name, category, price, stock, and image

3. Save product and verify in /api/products/

6️⃣ Manage Orders

1. View orders in Django Admin or via API /api/orders/

2. Update status (Pending → Processing → Shipped → Delivered)

7️⃣ Export Orders to CSV

Access /api/orders/export/ to generate downloadable CSV file of orders.

🧪 Testing (Admin-Focused)
| Test ID | Description                   | Endpoint                     | Expected Result |
| ------- | ----------------------------- | ---------------------------- | --------------- |
| TC-A1   | Admin login valid credentials | `/api/token/`                | 200 OK          |
| TC-A2   | Fetch product list            | `/api/products/`             | Paginated list  |
| TC-A3   | Add new product               | `/api/products/`             | 201 Created     |
| TC-A4   | Update product                | `/api/products/:id/`         | 200 OK          |
| TC-A5   | Delete product                | `/api/products/:id/`         | 204 No Content  |
| TC-A6   | Get pending orders            | `/api/orders?status=Pending` | 200 OK          |
| TC-A7   | Update order status           | `/api/orders/:id/status/`    | 200 OK          |
| TC-A8   | Unauthorized access           | `/api/admin/*`               | 401/403 Error   |

📊 Dashboard Summary

1. Total Orders

2. Total Revenue

3. Total Products

4. Pending Orders

All available through admin interface or API endpoints.

🧾 Sample Admin Credentials
| Field    | Value                                         |
| -------- | --------------------------------------------- |
| Email    | admin@example.com                             |
| Password | Admin@12345                                   |


🛡️ Security Notes

1. JWT Authentication for all protected routes

2. Role-based admin access control

3. Input validation and safe ORM queries

4. .env file excluded via .gitignore


### Deployment on Render
1. Go to https://render.com
2. Log in with your GitHub
3. Click “New” → “Web Service”
4. Choose this repo `ecommerce-mini`
5. Fill form:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn backend.wsgi`
