from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import RefreshView 

urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('api/auth/register', RegisterView.as_view(), name='register_user')
]