from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    mileage = models.FloatField()
    v_type = models.CharField(max_length=50)
    seats = models.IntegerField()
    v_seat_type = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    o_contact = models.BigIntegerField()
    feedback = models.TextField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"



