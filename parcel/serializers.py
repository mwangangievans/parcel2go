from rest_framework import serializers
from . import models


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parcel
        fields = "__all__"
