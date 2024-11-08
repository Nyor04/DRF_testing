from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from ipdb import set_trace

from drf_spectacular.utils import extend_schema_view,extend_schema

from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .permissions import IsDoctor

from app_appointment.serializers import AppointmentSerializer

from app_appointment.models import Appointment

from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)

@extend_schema_view(
    list=extend_schema(tags=['Doctors']),
    retrieve=extend_schema(tags=["Doctors"]),
    create=extend_schema(tags=["Admin - Doctors"]),
    update=extend_schema(tags=["Admin - Doctors"]),
    partial_update=extend_schema(tags=["Admin - Doctors"]),
    destroy=extend_schema(tags=["Admin - Doctors"]),
)
class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=["post"], detail=True, url_path="set-on-vacation")
    @extend_schema(
        tags=["Admin - Doctors"],
        summary="Set: bool(True) to the  is_on_vacation attribute of a Doctor Object",
    )
    def set_on_vacation(self, request, pk=None):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"message": f"Vacation set ON to Dr. {doctor.first_name} {doctor.last_name}"})

    @action(methods=["post"], detail=True, url_path="set-off-vacation")
    @extend_schema(
        tags=["Admin - Doctors"],
        summary="Set: bool(False) to the is_on_vacation attribute of a Doctor Object",
    )
    def set_off_vacation(self, request, pk=None):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"message": f"Vacation set OFF to Dr. {doctor.first_name} {doctor.last_name}"})

    @action(
        methods=["post", "get", "delete"], 
        detail=True, 
        url_path="appointments/(?P<appointment_id>[^/.]+)?",
        serializer_class=AppointmentSerializer
    )
    @extend_schema(
        tags=["Admin - Doctors"],
        summary="Interact with Doctor's Appointments",
        description=(
            "GET: Retrieve the list of appointments for the doctor. "
            "POST: Create an appointment for the doctor. "
            "DELETE: Delete a specific appointment using appointment ID."
        ),
    )
    def appointment(self, request, pk=None, appointment_id=None):
        doctor = self.get_object()

        # POST - Crear una nueva cita
        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # GET - Obtener citas del doctor
        if request.method == 'GET':
            if appointment_id:
                # Obtener una cita específica
                try:
                    appointment = Appointment.objects.get(id=appointment_id, doctor=doctor)
                    serializer = AppointmentSerializer(appointment)
                    return Response(serializer.data)
                except Appointment.DoesNotExist:
                    return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
            else:
                # Obtener todas las citas del doctor
                appointments = Appointment.objects.filter(doctor=doctor)
                serializer = AppointmentSerializer(appointments, many=True)
                return Response(serializer.data)

        # DELETE - Eliminar una cita específica
        if request.method == 'DELETE':
            if not appointment_id:
                return Response({"error": "Appointment ID is required."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                appointment = Appointment.objects.get(id=appointment_id, doctor=doctor)
                appointment.delete()
                return Response({"message": "Appointment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            except Appointment.DoesNotExist:
                return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

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

@extend_schema_view(
    list=extend_schema(tags=['Department']),
    retrieve=extend_schema(tags=["Department"]),
    create=extend_schema(tags=["Admin - Department"]),
    update=extend_schema(tags=["Admin - Department"]),
    partial_update=extend_schema(tags=["Admin - Department"]),
    destroy=extend_schema(tags=["Admin - Department"]),
)
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

@extend_schema_view(
    list=extend_schema(tags=['DoctorAvailability']),
    retrieve=extend_schema(tags=["DoctorAvailability"]),
    create=extend_schema(tags=["Admin - DoctorAvailability"]),
    update=extend_schema(tags=["Admin - DoctorAvailability"]),
    partial_update=extend_schema(tags=["Admin - DoctorAvailability"]),
    destroy=extend_schema(tags=["Admin - DoctorAvailability"]),
)
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

@extend_schema_view(
    list=extend_schema(tags=['MedicalNotes']),
    retrieve=extend_schema(tags=["MedicalNotes"]),
    create=extend_schema(tags=["Admin - MedicalNotes"]),
    update=extend_schema(tags=["Admin - MedicalNotes"]),
    partial_update=extend_schema(tags=["Admin - MedicalNotes"]),
    destroy=extend_schema(tags=["Admin - MedicalNotes"]),
)
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
