from rest_framework.routers import DefaultRouter


from . import views
from .viewsets import (
    DoctorViewSet,
    DepartmentViewSet,
    DoctorAvailabilityViewSet,
    MedicalNoteViewSet,
)

router = DefaultRouter()
router.register(r"doctors", DoctorViewSet)
router.register(r"departments", DepartmentViewSet)
router.register(r"availability", DoctorAvailabilityViewSet)
router.register(r"mediacal-notes", MedicalNoteViewSet)

urlpatterns = router.urls
