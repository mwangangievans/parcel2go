from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", views.ParcelModelViewSet, basename="parcel")
urlpatterns = [] + router.urls
