from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from ipdb import set_trace

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


class DoctorViewSet(ModelViewSet):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsDoctor]

    @action(["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"message":f"vacation set ON to Dr. {doctor.first_name + ' ' + doctor.last_name}"})
    

    @action(["POST"], detail=True, url_path="set-off-vacation")
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
     
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"message":f"vacation set OFF to Dr. {doctor.first_name + ' ' + doctor.last_name}"})
    ###tengo que implementar poder eliminar un appointment

    @action(['POST','GET','DELETE'], detail=True, serializer_class=AppointmentSerializer, url_path="appointments(?:/(?P<appointment_id>[^/.]+))?")
    def appointment(self, request, pk = None, appointment_id = None):
        doctor = self.get_object()
        
        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            if appointment_id == None:
                appointments = Appointment.objects.filter(doctor=doctor)

            if appointment_id != None:
                appointments = Appointment.objects.filter(doctor=doctor,id=appointment_id)
                
            serializer = AppointmentSerializer(data=appointments, many = True)
            serializer.is_valid()
            return Response(serializer.data)
        
        if request.method == 'DELETE':
            Appointment.objects.get(id=appointment_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

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
