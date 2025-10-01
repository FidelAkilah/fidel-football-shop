import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('apparel', 'Apparel'),
        ('equipment', 'Equipment'),
        ('accessories', 'Accessories'),
        ('fitness', 'Fitness'),
        ('outdoor', 'Outdoor'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='equipment')
    stock = models.PositiveIntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_popular(self):
        return self.product_views > 50
        
    @property
    def is_in_stock(self):
        return self.stock > 0
        
    @property
    def formatted_price(self):
        return f"Rp {self.price:,}"
        
    def increment_views(self):
        self.product_views += 1
        self.save()
        
    class Meta:
        ordering = ['-created_at']

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 255)

class Author(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    books = models.ManyToManyField(Books)