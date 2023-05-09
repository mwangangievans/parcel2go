from rest_framework import serializers
from . import models


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parcel
        fields = "__all__"


class SendSmsSerializer(serializers.Serializer):
    message = serializers.CharField()
    phone_numbers = serializers.ListField()
