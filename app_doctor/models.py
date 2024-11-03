from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.TextField()
    biography = models.TextField()

class Department(models.Model):
    doctor =models.ForeignKey(
        Doctor, 
        related_name='Department', 
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=50)
    description = models.TextField()

class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        related_name='availabilities',
        on_delete=models.CASCADE
        )
    start_date =models.DateField( auto_now=False, auto_now_add=False)
    end_date =models.DateField( auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

class MedicalNote(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        related_name='Medical_Notes',
        on_delete=models.CASCADE
        )
    note = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
