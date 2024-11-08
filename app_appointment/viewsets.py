from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema 
from .models import Appointment, AppointmentNote

from .serializers import (
    AppointmentSerializer,
    AppointmentNoteSerializer
        
)

@extend_schema_view(
    list=extend_schema(tags=['Appointment']),
    retrieve=extend_schema(tags=["Appointment"]),
    create=extend_schema(tags=["Admin - Appointment"]),
    update=extend_schema(tags=["Admin - Appointment"]),
    partial_update=extend_schema(tags=["Admin - Appointment"]),
    destroy=extend_schema(tags=["Admin - Appointment"]),
)
class AppointmentViewSet(ModelViewSet):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los Appointments."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un Appointment específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo Appointment."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un Appointment existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un Appointment existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un Appointment por su ID."""
        return super().destroy(request, *args, **kwargs)



@extend_schema_view(
    list=extend_schema(tags=['AppointmentNotes']),
    retrieve=extend_schema(tags=["AppointmentNotes"]),
    create=extend_schema(tags=["Admin - AppointmentNotes"]),
    update=extend_schema(tags=["Admin - AppointmentNotes"]),
    partial_update=extend_schema(tags=["Admin - AppointmentNotes"]),
    destroy=extend_schema(tags=["Admin - AppointmentNotes"]),
)
class AppointmentNoteViewSet(ModelViewSet):
    queryset = AppointmentNote.objects.all()
    serializer_class = AppointmentNoteSerializer

    def list(self, request, *args, **kwargs):
        """Devuelve una lista de todos los AppointmentNotes."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Devuelve un AppointmentNote específico por su ID."""
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Crea un nuevo AppointmentNote."""
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Actualiza completamente un AppointmentNote existente."""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Actualiza parcialmente un AppointmentNote existente."""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Elimina un AppointmentNote por su ID."""
        return super().destroy(request, *args, **kwargs)
