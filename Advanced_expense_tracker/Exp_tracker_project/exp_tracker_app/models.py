from django.db import models

# Create your models here.

class Expense(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=500)
    amount = models.IntegerField()
    category = models.CharField(max_length=500)
    date = models.DateField(auto_now=True) # this will set current date automatically
