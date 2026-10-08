from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor

from staff_v2.serializers import DoctorSerializers,UserSerializers
# Create your views here.

class DoctorListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,reuquest):

        qs = Doctor.objects.all() # query to python 

        seializers_instans = DoctorSerializers(qs,many=True)

        return Response(data=seializers_instans.data)

    def post(self,request):

        form_data = request.data

        serialization_instants = DoctorSerializers(data=form_data)

        if serialization_instants.is_valid():

            cleaned_data = serialization_instants.validated_data

            Doctor.objects.create(**cleaned_data)

            return Response(data=serialization_instants.validated_data)

        else:

            return Response(data=serialization_instants.errors)

class DoctorRetrieveUpdateDeleteView(APIView):

    
    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs = Doctor.objects.get(id=pk)

        serialization_instance = DoctorSerializers(qs)       

        return Response(data=serialization_instance.data) 

    def delete(self,request,pk=None):

        qs = Doctor.objects.get(id=pk)

        serialazation_instants = DoctorSerializers(qs)

        qs.delete()

        return Response(data=serialazation_instants.data)

    def put(self,requset,pk=None):

        form_data = requset.data

        serializer_instat = DoctorSerializers(data=form_data)

        if serializer_instat.is_valid():

            cleeane_data = serializer_instat.validated_data

            Doctor.objects.filter(id=pk).update(**cleeane_data)

            return Response(data=serializer_instat.validated_data)

        else:
            return Response(data=serializer_instat.errors)


class AdminRegister(APIView):

    def post(self,request):

        form_data = request.data

        serializers_instant = UserSerializers(data=form_data)

        if serializers_instant.is_valid():

            cleeaned_data = serializers_instant.validated_data

            User.objects.create_superuser(**cleeaned_data)

            return Response(data=serializers_instant.data)

        else:

            return Response(data=serializers_instant.errors)

