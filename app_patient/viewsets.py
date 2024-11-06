from rest_framework.viewsets import ModelViewSet
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class =  PatientSerializer


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