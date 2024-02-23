from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  ##Temporarily allowing null values
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True)

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CustomerReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
