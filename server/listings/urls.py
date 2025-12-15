from django.urls import path
from .views import ListListingsView, CreateListingView
urlpatterns = [
    path('', ListListingsView.as_view(), name='Listings'),
    path('', CreateListingView.as_view(), name='Crate Listings')

]