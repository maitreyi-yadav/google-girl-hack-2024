# from django.shortcuts import render
from api.serializers.doctor_serializer import DoctorSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.stop_words import specialties
from utils.process_text import find_diseases, find_diseases_detailed, check_input_validity
from api.models.hospital import *


class DoctorPredictionView(APIView):
    class Input_Serializer(serializers.Serializer):
        symptoms = serializers.CharField()

    def post(self, request, *args, **kwargs):
        result = []
        ser = self.Input_Serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        symptoms = request.data["symptoms"]
        if not check_input_validity(symptoms):
            return Response(
                data={"data": "Input text is not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        diseases = find_diseases_detailed(text_input=symptoms)

        if not diseases:
            return Response(
                data={
                    "data": "Insufficient information to find a doctor. Please try with more detail."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        for disease in diseases:
            for key, values in specialties.items():
                if disease in values:
                    res = {disease : key}
                    if res not in result:
                        result.append(res)
        r = result[:2]
        doctors = []
        for k in r:
            doc = Doctor.objects.filter(specialty__name_of_specialty=list(k.values())[0])
            doctors.append(DoctorSerializer(doc, many=True).data)
        return Response(data={"illness": result[:2], 'doctors':doctors}, status=status.HTTP_200_OK)

from django.shortcuts import render

def index(request):
    return render(request, 'frontend.html')