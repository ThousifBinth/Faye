from django.db import models
from seller.models import *

# Create your models here.


class Customerregistration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def  __str__(self):
        return self.name
    

class Cart(models.Model):
      customer=models.ForeignKey(Customerregistration,on_delete=models.CASCADE,null=True)
      product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
      quantity=models.PositiveIntegerField(default=1)


      