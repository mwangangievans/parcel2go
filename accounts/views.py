from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
