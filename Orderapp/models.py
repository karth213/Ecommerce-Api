from django.db import models
from django.contrib.auth.models import User
from app.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 99)
    last_name = models.CharField(max_length = 99)
    email = models.EmailField(null=True)
    Phone = models.CharField(max_length =10)
    place = models.CharField(max_length = 99)
    created_at = models.DateTimeField(auto_now_add = True)
    paid_amount = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null=True)
    srtipe_token = models.CharField(max_length=99)


    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.first_name
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'orederitem', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name= 'product', on_delete= models.CASCADE)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    quntity = models.IntegerField(default = 1)

    def __str__(self):
        return '%s' % self.id






