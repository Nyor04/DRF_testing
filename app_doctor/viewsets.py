from rest_framework.viewsets import ModelViewSet

from .models import Doctor, Department, DoctorAvailability, MedicalNote

from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)


class DoctorViewSet(ModelViewSet):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los Doctores."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un Doctor específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo Doctor."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un Doctor existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un Doctor existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un Doctor por su ID."""
        return super().destroy(request, *args, **kwargs)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los Departments."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un Department específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo Department."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un Department existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un Department existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un Department por su ID."""
        return super().destroy(request, *args, **kwargs)


class DoctorAvailabilityViewSet(ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los DoctorAvailabilities."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un DoctorAvailability específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo DoctorAvailability."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un DoctorAvailability existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un DoctorAvailability existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un DoctorAvailability por su ID."""
        return super().destroy(request, *args, **kwargs)


class MedicalNoteViewSet(ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los MedicalNotes."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un MedicalNote específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo MedicalNote."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un MedicalNote existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un MedicalNote existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un MedicalNote por su ID."""
        return super().destroy(request, *args, **kwargs)