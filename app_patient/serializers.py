from rest_framework import serializers
from .models import Patient, Insurance, MediacalRecord
from app_appointment.serializers import AppointmentSerializer

class PatientSerializer(serializers.ModelSerializer):

    appointments = AppointmentSerializer(many= True, read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments'
        ]

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class MediacalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediacalRecord
        fields = '__all__'