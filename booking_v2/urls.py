from django.urls import path

from booking_v2.views import SignUpRegisterView,AppointmentListCreateView,AppointmentRetriveUpdateDeleteView

urlpatterns = [

    path('signup/',SignUpRegisterView.as_view()),

    path('appointment/',AppointmentListCreateView.as_view()),
    path('appointment/<int:pk>/',AppointmentRetriveUpdateDeleteView.as_view()),
    
]