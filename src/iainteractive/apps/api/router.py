"""Api Router"""


from rest_framework.routers import DefaultRouter

from iainteractive.apps.api.viewsets import ApplicantViewSet

router = DefaultRouter()
router.register(r"applicants", ApplicantViewSet, basename="user")

urlpatterns = router.urls
