from django.contrib.auth.models import User

from rest_framework import serializers

from staff.models import Doctor

class DoctorSerializers(serializers.ModelSerializer):

    class Meta:

        model = Doctor

        fields = '__all__'

        read_only_fields =["id"]

    #implementing validation

    def validate(self,validate_data):

        fee = validate_data.get("fee")

        if fee < 250:

            raise serializers.ValidationError("invalid fee should bee > 250")

        else:
            return validate_data

class UserSerializers(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

    
