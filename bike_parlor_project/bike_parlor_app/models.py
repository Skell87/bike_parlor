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

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    # want to set to null, cascade will delete the customer too. needs null=true to work
    vehicles = models.ManyToManyField(Vehicle)
    # can add related_name="such n such " to reference info both ways.
    paid_status = models.BooleanField()

    def __str__(self):
        v_list= ""
        for v in self.vehicles.all():
            v_list += f'{v.make} {v.model} {v.type} {v.color} {v.price} {v.number_in_stock}'
        return f'NAME: {self.customer.first_name} {self.customer.last_name} BIKE: {v_list} IS PAID: {self.paid_status}'
    

    