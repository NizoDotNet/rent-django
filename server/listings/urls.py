from django.urls import path
from .views import CreateListListingsView
urlpatterns = [
    path('', CreateListListingsView.as_view(), name='create-list-listings'),

]