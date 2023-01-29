"""Common Admin Module"""

from django.contrib import admin
from iainteractive.apps.common.models import Grimorie, MagicAffinity, Applicant


admin.site.register(Grimorie)
admin.site.register(MagicAffinity)
admin.site.register(Applicant)