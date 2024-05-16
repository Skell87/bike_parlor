from django.db import models
from django.utils import timezone

# Create your models here.

class Vehicle(models.Model):
    make = models.TextField()
    model = models.TextField()
    type = models.TextField()
    color = models.TextField()
    price = models.IntegerField()
    number_in_stock = models.IntegerField()
    
    def __str__(self):
        return f'MAKE: {self.make}, MODEL: {self.model}, TYPE: {self.type}, COLOR: {self.color}, PRICE: {self.price}, STOCK: {self.number_in_stock}'

class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    def __Str__(self):
        return f'First Name: {self.first_name}, Last Name: {self.last_name}'

# class CustomerOrder(models.Model):
#     customer = models.TextField()
#     order = models.TextField()
#     modified_date = models.DateTimeField()
#     created_date  = models.DateTimeField(editable=False)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.created_date = timezone.now()
#         self.modified_date = timezone.now
#         return super(CustomerOrder, self).save(*args, **kwargs)