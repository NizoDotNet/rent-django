from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Authentication'])
class LoginView(TokenObtainPairView):
    ...