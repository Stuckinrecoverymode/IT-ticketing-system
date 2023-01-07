from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    device_name = models.CharField(max_length=100)
    customer_mail = models.EmailField()
    customer_type = models.CharField(max_length=50)
    submitted_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_submitted = models.DateTimeField(auto_now_add=True)
    device_state = models.CharField(max_length=10)
    device_problem = models.CharField(max_length=100)

class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)