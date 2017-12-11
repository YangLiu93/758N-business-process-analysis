from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import uuid

class Orders(models.Model):
    OrderId = models.CharField(max_length=250)
    TimeStamp = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)

class Product(models.Model):
    ProdId = models.CharField(max_length=100)
    PName = models.CharField(max_length=100)
    PType = models.CharField(max_length=250)
    PCat = models.CharField(max_length=100)
    PPrice = models.CharField(max_length=250)
    PQuantity = models.CharField(max_length=250)
    Prourl = models.CharField(max_length=500)
    ProBuyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.PName

class ProductOrder(models.Model):
    ProdOrderId = models.CharField(max_length=250)
    ReturnStatus = models.CharField(max_length=100)
    OrderQuantity = models.CharField(max_length=500)
    CurrentQuantity = models.CharField(max_length=500)
    TotalPrice = models.CharField(max_length=500)
    OrderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProdId = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProdOrderId + "-" + self.Orders.OrderId

class return_order(models.Model):
    ReturnId = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    RTimeStamp = models.DateTimeField(auto_now_add=True)
    ReturnReason_choices = (
        ('Product Damaged','Product Damaged'),
        ('Item arrived too late','Item arrived too late'),
        ('Missing Parts or accesories','Missing Parts or accesories'),
        ('Product and shipping box both damaged','Product and shipping box both damaged'),
        ('Wrong item sent','Wrong item sent'),
        ('Item defective', 'Item defective'),
        ('Item no longer needed','Item no longer needed'),
    )
    ReturnReason = models.CharField(max_length=500, choices=ReturnReason_choices)
    ReturnOption_choices = (
        ('Cashback','Cashback'),
        ('Replacement','Replacement'),
        ('EKart Credits','EKart Credits'),
    )
    ReturnOptions = models.CharField(max_length=500, choices=ReturnOption_choices)
    #ReturnFeedback = models.CharField(max_length=500)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    #ProductName = models.CharField(max_length=500)
    ProductQuality_choices = (
        ('Excellent - Unopened','Excellent - Unopened'),
        ('Good - Slightly Used','Good - Slightly Used'),
        ('Poor - Broken','Poor - Broken')
    )
    ProductQuality = models.CharField(max_length=500, choices=ProductQuality_choices)

    def get_absolute_url(self):
        return reverse ('order:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.ReturnId + "-" + self.RTimeStamp



