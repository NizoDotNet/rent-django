from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import RefreshView 
from .views import GetRoleView

urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', RefreshView.as_view(), name='token_refresh'),
    path('api/auth/register', RegisterView.as_view(), name='register_user'),
    path('api/auth/role', GetRoleView.as_view(), name='get_role')

]