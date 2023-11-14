from django.db import models

# Create your models here.

class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    university = models.CharField(max_length=500)
    previous_work = models.TextField(max_length=2000)
    skills = models.TextField(max_length=2000)
    strength = models.TextField(max_length=2000)
    project = models.TextField(max_length=2000)
    address = models.TextField(max_length=2000)
    nationalityy = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=200)
    date = models.DateField()
    place = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)