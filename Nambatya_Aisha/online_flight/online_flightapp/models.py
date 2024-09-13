from django.db import models
from datetime import datetime

class FlightPassenger(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth = models.DateField(default=datetime.now, null=True, blank=False)
    nationality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    po_box = models.CharField(max_length=100, null=True, blank=True)
    emergency_phone = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=20)
    visa_document = models.FileField(upload_to='visas/')
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
