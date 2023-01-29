"""Common Urls module"""

# Django
from django.urls import path

# Common
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
]
