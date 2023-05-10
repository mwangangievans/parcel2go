from rest_framework import serializers

from accounts.serializers import UserSerializer
from . import models


class ParcelSerializer(serializers.ModelSerializer):
    sender  = UserSerializer()
    receiver = UserSerializer()
    
    class Meta:
        model = models.Parcel
        fields = "__all__"


class SendSmsSerializer(serializers.Serializer):
    message = serializers.CharField()
    phone_numbers = serializers.ListField()
