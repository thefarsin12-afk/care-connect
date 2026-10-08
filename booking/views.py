from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from booking.models import Appointment
from booking.serializer import AppointementSerailizer
from staff.models import Doctor
# Create your views here.


class AppoinmentListCreateView(APIView):

    def get(self,requset):

        qs = Appointment.objects.all()

        serializer_instant = AppointementSerailizer(qs,many=True)

        return Response(data=serializer_instant.data)

    def post(self,request):

        form_data=request.data

        serializer_instance=AppointementSerailizer(data=form_data)

        if serializer_instance.is_valid():
                
            cleened_data = serializer_instance.validated_data

            doctor = cleened_data.get("doctor")

            appointment_date = cleened_data.get("appointment_date")

            new_token = 0

            last_appoinmenet_object = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()

            if last_appoinmenet_object:

                new_token = last_appoinmenet_object.token_number + 1

            else:

                new_token = 1

            doctor_object = Doctor.objects.get(id=fdoctor)

            cleened_data["doctor"]=doctor_object

            Appointment.objects.create(**cleened_data,token_number = new_token)

            response_data = {

                "status":"booked",
                "token":new_token
            }
            return Response(data=response_data)

        else:
            return Response(data=serializer_instance.errors)

           




            