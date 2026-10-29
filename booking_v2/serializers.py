from rest_framework import serializers

from django.contrib.auth.models import User

from booking.models import Appointment

from datetime import datetime

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class AppointmentSerializer(serializers.ModelSerializer):

    
    class Meta:

        model = Appointment

        fields = '__all__'

        read_only_field = ["id","token_number","appointment_time","created_at"]


    def validate(self, validate_data):

        appointment_date = validate_data.get("appointment_date")

        doctor = validate_data.get("doctor")

        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("Date should be greater than or equal to current date" )

        last_appointment_object = Appointment.objects.filter( doctor=doctor,appointment_date=appointment_date).last()

        if last_appointment_object:

            if last_appointment_object.token_number == 25:

                raise serializers.ValidationError("Token full... book to next day")

        return validate_data