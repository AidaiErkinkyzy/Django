

from .views import *
from django.urls import path

urlpatterns = [
    path("contact_us/", ContactUsView.as_view(), name="contact_us")
]

