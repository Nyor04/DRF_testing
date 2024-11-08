from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
urlpatterns = [
    # YOUR PATTERNS
    path(r'schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(r'', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(r'schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]