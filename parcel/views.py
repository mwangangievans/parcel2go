from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from .utils import send_sms
from rest_framework import status


# Create your views here.
class ParcelModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Parcel.objects.all()
    serializer_class = serializers.ParcelSerializer


class SendBulkSmsApiView(generics.GenericAPIView):
    serializer_class = serializers.SendSmsSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sms = serializer.data["message"]
        phone_numbers = serializer.data["phone_numbers"]
        try:
            send_sms(sms, phone_numbers)
            return Response({"msg": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
