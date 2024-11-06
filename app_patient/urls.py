from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register(r'patients',PatientViewSet)

urlpatterns = router.urls
