from rest_framework import serializers
from .models import Appointment, MedicalNote

class AppointmentSerializer(serializers.ModelSerializer):
    class meta:
        model = Appointment
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class meta:
        model = MedicalNote
        fields = '__all__'