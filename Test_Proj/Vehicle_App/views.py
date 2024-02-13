from django.shortcuts import render
from Vehicle_App.models import Vehicle
from Vehicle_App.serializers import VehicleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
#Create your views here.
class VehicleListAPIView(APIView):
    def get(self, request, format=None):
        qs = Vehicle.objects.all()
        serializer = VehicleSerializer(qs, many=True)
        return Response(serializer.data)
