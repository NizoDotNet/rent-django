from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



urlpatterns = [
    path(r'api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(r'api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(r'api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path(r'api/auth/', include('accounts.urls')),
    path(r'api/listings/', include('listings.urls'))
]