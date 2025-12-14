from django.urls import path
from .views.RegisterView import RegisterView
from .views.LoginView import LoginView
from .views.RefreshView import RefreshView 

urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('api/auth/register', RegisterView.as_view(), name='register_user')
]