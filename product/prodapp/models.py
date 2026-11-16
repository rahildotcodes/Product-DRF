from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    stock=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
