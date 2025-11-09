# from django.db import models

# # Create your models here.
# from django.db import models
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     # slug = models.SlugField(unique=True)
#     # category = models.CharField(max_length=100)
#     # weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField(default=0)
#     images = models.ImageField(upload_to='products/', null=True, blank=True)  # or separate Image model for multiple
#     description = models.TextField(blank=True)
#     # is_active = models.BooleanField(default=True)  # soft-delete support
#     # created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.name





# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField(default=0)
#     images = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     is_active = models.BooleanField(default=True)  # 👈 add this line
#     created_at = models.DateTimeField(auto_now_add=True)  # 👈 optional (since your view orders by this)

#     def __str__(self):
#         return self.name



from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('home', 'Home'),
        ('books', 'Books'),
        ('toys', 'Toys'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    images = models.ImageField(upload_to='product_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, default='General')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
