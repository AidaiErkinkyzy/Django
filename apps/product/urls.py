
from django.urls import path
from .views import *

urlpatterns = [
    path("product_list/", ProductListView.as_view(), name="product_list")
]









