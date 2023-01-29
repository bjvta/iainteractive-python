"""Common Views module"""

# Django
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "common/home.html"

