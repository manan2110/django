from django.db import models

# Create your models here.

class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30,default="Available")
    City = models.CharField(max_length=30)
    Phone = models.CharField(max_length=13)
    Email = models.CharField(max_length=30)
    GitHub = models.CharField(max_length=30)
    Languages = models.CharField(max_length=30)

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    your_name = models.CharField(max_length=20)
    your_email = models.CharField(max_length = 20)
    your_subject = models.CharField(max_length=20)
    your_message = models.TextField()