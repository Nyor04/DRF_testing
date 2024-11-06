from rest_framework.routers import DefaultRouter


from . import views
from .viewsets import (
   AppointmentViewSet,
   AppointmentNoteViewSet
)

router = DefaultRouter()
router.register(r"appointment", AppointmentViewSet)
router.register(r"appointment-notes", AppointmentNoteViewSet)

urlpatterns = router.urls
