from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import RefreshView 
from .views import GetRoleView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', RefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register_user'),
    path('role/', GetRoleView.as_view(), name='get_role')

]