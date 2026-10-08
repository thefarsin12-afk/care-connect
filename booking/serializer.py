from rest_framework import serializers

from datetime import datetime

from booking.models import Appointment

class AppointementSerailizer(serializers.ModelSerializer):

    class Meta:

        model = Appointment

        fields = '__all__'

        read_only = ["id","token_number","appointment_time","created_at"]


    def validate(self,validated_data):

        appointment_date = validated_data.get("appointment_date")

        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("Invalid date")

        return validated_data