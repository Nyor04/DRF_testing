from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Insurance, MediacalRecord

from .serializers import (
    PatientSerializer,
    InsuranceSerializer,
    MediacalRecordSerializer,
)


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(['GET'], detail=True, url_path='get-medical-history')
    def get_medical_history(self, request, pk):
        patient = self.get_object()
        return Response({f"patient_{patient.first_name + '_' + patient.last_name}_medical_history":f"{patient.medical_history}"})

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los pacientes."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un paciente específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo paciente."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un paciente existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un paciente existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un paciente por su ID."""
        return super().destroy(request, *args, **kwargs)


"""
mas adelante quisiera que la informacion solicitada de los seguros sea exclusiva del usuario que esta haciendo la solicitud
por ende modificare el metodo get_queryset, pasando self como argumento, de self puedo sacar el atributo request, por ende el user. 
estos endpoints deben requerir que el usuario este autenticado.
"""


class InsuranceViewSet(ReadOnlyModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los seguros."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un seguro específico por su ID."""
        return super().retrieve(request, *args, **kwargs)


class MediacalRecordViewSet(ReadOnlyModelViewSet):
    queryset = MediacalRecord.objects.all()
    serializer_class = MediacalRecordSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista todos los records medicos"""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un el record medico de un paciente específico por su ID."""
        return super().retrieve(request, *args, **kwargs)
