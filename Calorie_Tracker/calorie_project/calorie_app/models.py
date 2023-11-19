from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

class Consume(models.Model):
    '''
    This model is created to understand which user consumed which food item or added which food item
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE) # this connects 2 models User and Consume to  know which user consumed which food item.
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE) # this connects 2 models Food and Consume to  know which user added which food item.
