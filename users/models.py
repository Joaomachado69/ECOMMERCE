from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import logging
from .tasks import recalcula_avaliacao_media_produto


recalcula_avaliacao_media_produto.delay(produto_id)
#celery -A seu_projeto worker -l info


logger = logging.getLogger(__name__)

class Product(models.Model):
    # Seu código de modelo aqui...

    def save(self, *args, **kwargs):
        logger.info(f"Produto '{self.name}' foi salvo.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        logger.info(f"Produto '{self.name}' foi deletado.")
        super().delete(*args, **kwargs)

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
