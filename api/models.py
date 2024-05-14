from django.db import models

# Create your models here.
class Bookings(models.Model):
  BookingId = models.IntegerField()  
  CustomerName  = models.CharField(max_length=100)
  RoomNumber= models.IntegerField()
  CheckingDate= models.DateTimeField()
  CheckoutOrder = models.DateTimeField()
  TotalPrice    = models.DecimalField(max_digits=5, decimal_places=2)

class Customer(models.Model):
  CustomerId = models.IntegerField()  
  CustomerName  = models.CharField(max_length=100)
  RoomNumber= models.IntegerField()
  CheckingDate= models.DateTimeField()
  NumberOfcustomers = models.IntegerField()
   