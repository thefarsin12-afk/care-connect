from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from staff.models import Doctor

class DoctorListCreateView(APIView):

    def get(self,request):

        qs = Doctor.objects.all().values()

        lst_data = list(qs)

        return Response (data = lst_data)

    def post(self,request):

        form_data = request.data
        
        Doctor.objects.create(**form_data)

        return Response({"message":"created"})

class retrieveupdatedelete(APIView):

    def get(self,request,pk=None):

        qs = Doctor.objects.filter(id=pk).values()    



