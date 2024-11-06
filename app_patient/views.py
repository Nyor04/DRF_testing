from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Patient
from .serializers import PatientSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def get_patients(request):
#     patients = Patient.objects.all()
#     serializer = PatientSerializer(patients, many=True)
#     return Response(serializer.data)

# # Create your views here.
# class PatientClassView(CreateAPIView, ListAPIView):
#     allowed_methods = ['GET', 'POST']
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
