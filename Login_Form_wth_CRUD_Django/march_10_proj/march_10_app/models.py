from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=300)