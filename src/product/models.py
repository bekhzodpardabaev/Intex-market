from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    sale = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    frame = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    width = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.category.name} {self.sale} sum"


class Order(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Consultation(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
