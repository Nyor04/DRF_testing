from rest_framework import serializers
from .models import Patient, Insurance, MediacalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class MediacalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediacalRecord
        fields = '__all__'