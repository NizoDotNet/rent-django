from django.urls import path
from .views import BookingView, BookingApproveView, BookingRejectView
urlpatterns = [
    path('', BookingView.as_view(), name='create-booking'),
    path('<int:id>/approve', BookingApproveView.as_view(), name='approve-booking'),
    path('<int:id>/reject', BookingRejectView.as_view(), name='approve-reject'),

]