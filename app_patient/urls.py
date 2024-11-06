from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views
from .viewsets import PatientViewSet, InsuranceViewSet, MediacalRecordViewSet

router = DefaultRouter()
router.register(r"patients", PatientViewSet)
router.register(r"insurance", InsuranceViewSet)
router.register(r"medical-record", MediacalRecordViewSet)

urlpatterns = router.urls
