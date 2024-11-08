from django.db import models
from app_doctor.models import Doctor
from app_patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        related_name='appointments', 
        on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor,
        related_name='appointments', 
        on_delete=models.CASCADE)
    apointment_date = models.DateField( auto_now=False, auto_now_add=False)
    apointment_time = models.TimeField( auto_now=False, auto_now_add=False)
    notes = models.TextField()
    pending = models.BooleanField(default=True)


class AppointmentNote(models.Model):
    appointment_note = models.ForeignKey(
        Appointment,
        related_name="appointment_notes",
        on_delete=models.CASCADE)
    notes = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)