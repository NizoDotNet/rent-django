from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import RefreshView 
from .views import GetRoleView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='token_obtain_pair'),
    path(r'refresh/', RefreshView.as_view(), name='token_refresh'),
    path(r'register/', RegisterView.as_view(), name='register_user'),
    path(r'role/', GetRoleView.as_view(), name='get_role')

]