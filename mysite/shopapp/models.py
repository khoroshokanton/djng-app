from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=100)
    discription = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    products = models.ManyToManyField(Product, related_name="orders")
