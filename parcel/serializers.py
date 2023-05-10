from rest_framework import serializers

from accounts.serializers import UserSerializer
from . import models


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parcel
        fields = "__all__"
        
    def to_representation(self, instance):
        self.fields["sender"] = UserSerializer()
        self.fields["receiver"] = UserSerializer()
        return super(ParcelSerializer, self).to_representation(instance)


class SendSmsSerializer(serializers.Serializer):
    message = serializers.CharField()
    phone_numbers = serializers.ListField()
