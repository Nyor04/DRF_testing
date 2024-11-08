from rest_framework import serializers
from .models import Doctor, Department,DoctorAvailability,MedicalNote
from app_appointment.serializers import AppointmentSerializer

class DoctorSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many= True, read_only=True)
    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'qualifications',
            'contact_number',
            'email',
            'address',
            'biography',
            'is_on_vacation',
            'appointments'
        ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'
