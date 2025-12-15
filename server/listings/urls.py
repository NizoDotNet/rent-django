from django.urls import path
from .views import CreateListListingsView, RetrieveUpdateDestroyListingView
urlpatterns = [
    path('', CreateListListingsView.as_view(), name='create-list-listings'),
    path('<int:id>', RetrieveUpdateDestroyListingView.as_view(), name='retrieve-update-destroy-listing')
]