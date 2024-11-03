from rest_framework import serializers
from .models import Doctor, Department,DoctorAvailability,MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class meta:
        model = MedicalNote
        fields = '__all__'
