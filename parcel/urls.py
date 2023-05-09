from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", views.ParcelModelViewSet, basename="parcel")
urlpatterns = [
    path("send_sms/", views.SendBulkSmsApiView.as_view(), name="send_sms")
] + router.urls
