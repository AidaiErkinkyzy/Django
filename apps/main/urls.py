


from django.urls import path
from .views import *



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about_us", AboutUsView.as_view(), name="about_us"),
]

