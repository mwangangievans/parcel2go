from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class RegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User(
                username=serializer.data["username"],
                email=serializer.data["email"],
                password=make_password(serializer.data["password"]),
            )
            user.save()
            response_data = {"msg": "success"}
        except Exception as e:
            response_data = {"error": f"{str(e)}"}
        return Response(response_data, status.HTTP_201_CREATED)


class LoginApiView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                )
            else:
                return Response(
                    {"error": "Invalid email or password"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        try:
            user.first_name = serializer.data["first_name"]
            user.last_name = serializer.data["last_name"]
            user.address = serializer.data["address"]
            user.photo = serializer.data["photo"]
            user.phone_number = serializer.data["phone_number"]
            user.save()
            response_data = self.get_serializer(user).data
        except Exception as e:
            response_data = {"error": f"{str(e)}"}
        return Response(response_data, status.HTTP_201_CREATED)

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
