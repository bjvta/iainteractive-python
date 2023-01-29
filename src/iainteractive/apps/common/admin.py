"""Common Admin Module"""

from django.contrib import admin

from iainteractive.apps.common.models import Applicant, Grimorie, MagicAffinity

admin.site.register(Grimorie)
admin.site.register(MagicAffinity)
admin.site.register(Applicant)
