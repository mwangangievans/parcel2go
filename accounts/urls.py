from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", views.UserViewSet, basename="user")
urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("login/", views.LoginApiView.as_view(), name="login"),
    path("profile/", views.ProfileApiView.as_view(), name="profile")
    ] 
