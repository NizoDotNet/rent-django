from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token

@extend_schema(tags=['Authentication'])
class LoginView(TokenObtainPairView):
    ...

