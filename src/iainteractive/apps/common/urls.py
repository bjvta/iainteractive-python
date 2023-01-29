"""Common Urls module"""

# Django
from django.conf.urls import url

# Common
from .views import *


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_view'),
]