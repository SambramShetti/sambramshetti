from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
