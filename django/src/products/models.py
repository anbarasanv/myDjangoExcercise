from django.db import models

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)#mandatory 
    description     = models.TextField(null=True)
    price           = models.DecimalField(decimal_places=2,max_digits=1000)
    summery         = models.TextField()
    featured        = models.BooleanField(default = True) #null = True, default = True
