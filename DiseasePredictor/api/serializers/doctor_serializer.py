from rest_framework import serializers
from api.models.hospital import *

class DoctorSerializer(serializers.ModelSerializer):
    specialty_name = serializers.CharField(source='specialty.name_of_specialty', read_only=True)
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)
    class Meta:
        model = Doctor
        fields = ["name", "experience", "days_available", "time_available", "specialty_name", "hospital_name"]

